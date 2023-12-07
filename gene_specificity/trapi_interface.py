'''trapi interface'''
import uuid
import json
import pkgutil
import logging
from typing import Tuple, Union
from django.db.models import QuerySet
from pydantic import parse_obj_as
from reasoner_pydantic.utils import HashableMapping
from reasoner_pydantic import MetaKnowledgeGraph, Message, KnowledgeGraph
from reasoner_pydantic.kgraph import RetrievalSource, Attribute
from reasoner_pydantic.results import NodeBinding, EdgeBinding, Result, Results, Analysis
from gene_specificity.models import TissueToGene, GeneToTissue, CurieTemplate, CurieTemplateMatch

# Setup logging
logging.addLevelName(25, "NOTE")
# Add a special logging function
def note(self, message, *args, **kwargs):
    self._log(25, message, args, kwargs)
logging.Logger.note = note
internal_logger = logging.getLogger(__name__)

class TrapiInterface:
    def __init__(self, trapi_version: str = '1.4'):
        self.trapi_version = trapi_version

    def get_meta_knowledge_graph(self) -> MetaKnowledgeGraph:
        return self._read_meta_knowledge_graph()

    def _read_meta_knowledge_graph(self) -> MetaKnowledgeGraph:
        meta_kg_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'app_meta_data/meta_knowledge_graph.json'
        )
        meta_kg_str = meta_kg_bytes.decode('utf-8')
        meta_kg_json = json.loads(meta_kg_str)
        meta_kg = MetaKnowledgeGraph.parse_obj(meta_kg_json)
        return meta_kg

    def get_name(self) -> str:
        return 'gene_specificity'

    def _get_sources(self):
        source_1 = RetrievalSource(resource_id = "infores:connections-hypothesis",
                                   resource_role="primary_knowledge_source")
        source_2 = RetrievalSource(resource_id = "infores:gtex",
                                   resource_role="supporting_data_source")
        return {source_1, source_2}

    def _get_attributes(self, spec_val, norm_spec_val, p_val):
        att_1 = Attribute(attribute_type_id = 'Specificity (Normalized)',
                          value_type_id='biolink:has_evidence',
                          value=norm_spec_val,
                          description="Specificity values for gene->tissue measure the specificity of a gene's transcription across all tissues. Specificity values for tissue->gene measure specificity of all gene's transcription in a tissue.")
        att_2 = Attribute(attribute_type_id = 'Specificity (Unnormalized)',
                          value_type_id='biolink:has_evidence',
                          value=spec_val,
                          description="Specificity values for gene->tissue measure the specificity of a gene's transcription across all tissues. Specificity values for tissue->gene measure specificity of all gene's transcription in a tissue.")
        att_3 = Attribute(attribute_type_id = 'Specificity P-value',
                          value_type_id='biolink:has_evidence',
                          value=p_val,
                          description="P-val assessing significance of unnormalized Specificity value.")
        att_4 = Attribute(attribute_type_id = 'primary_knowledge_source',
                          value='infores:connections-hypothesis',
                          value_url='https://github.com/di2ag/gene-specificity',
                          description='The Connections Hypothesis Provider from NCATS Translator')
        return {att_1, att_2, att_3, att_4}

    def _add_results(self, message, subject_mapping, qg_subject_id, subject_curies, subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, object_curies, object_category, spec_vals, norm_spec_vals, p_vals):
        node_binding_group = []
        edge_binding_group = []
        nodes = dict()
        edges = dict()
        val_id = 0
        for subject_curie in subject_curies:
            for object_curie in object_curies:
                nodes[subject_curie] = {"categories": [subject_category]}
                nodes[object_curie] = {"categories": [object_category]}
                kg_edge_id = str(uuid.uuid4())
                spec_val = spec_vals[val_id]
                norm_spec_val = norm_spec_vals[val_id]
                p_val = p_vals[val_id]
                edges[kg_edge_id] = {"predicate": predicate,
                                     "subject": subject_curie,
                                     "object": object_curie,
                                     "sources": self._get_sources(),
                                     "attributes": self._get_attributes(spec_val, norm_spec_val, p_val)}
                val_id += 1

                node_bindings = {qg_subject_id: set(), qg_object_id: set()}
                edge_bindings = {qg_edge_id : set()}
                if subject_curie in subject_mapping:
                    node_bindings[qg_subject_id].add(NodeBinding(id = subject_curie, query_id = subject_mapping[subject_curie]))
                else:
                    node_bindings[qg_subject_id].add(NodeBinding(id = subject_curie))
                if object_curie in object_mapping:
                    node_bindings[qg_object_id].add(NodeBinding(id = object_curie, query_id = object_mapping[object_curie]))
                else:
                    node_bindings[qg_object_id].add(NodeBinding(id = object_curie))
                edge_bindings[qg_edge_id].add(EdgeBinding(id = kg_edge_id))
                node_binding_group.append(node_bindings)
                edge_binding_group.append(edge_bindings)
        kgraph = KnowledgeGraph(nodes=nodes, edges=edges)
        if message.knowledge_graph is not None:
            message.knowledge_graph.update(kgraph)
        else:
            message.knowledge_graph = kgraph
        return node_binding_group, edge_binding_group

    def _get_curie_descendants(self, qnode):
        ids = qnode.ids
        category = qnode.categories[0]
        if ids is not None:
            mapping = dict()
            descendant_curies = set()
            for id in ids:
                matches = CurieTemplateMatch.objects.filter(curie_template__curie=id)
                for match in matches:
                    descendant_curies.add(match.curie)
                    if id != match.curie:
                        mapping[match.curie] = id
            return mapping, list(descendant_curies), category
        return dict(), None, category

    def get_response(self, message: Message, logger):
        for edge_id, edge in message.query_graph.edges.items():
            predicate = edge.predicates[0]
            qg_edge_id = edge_id
            qg_subject_id = edge.subject
            qg_object_id = edge.object
        subject_mapping, subject_curies, subject_category = self._get_curie_descendants(message.query_graph.nodes[qg_subject_id])
        object_mapping, object_curies, object_category = self._get_curie_descendants(message.query_graph.nodes[qg_object_id])
        # annotation
        node_bindings = []
        edge_bindings = []
        if subject_curies is not None and object_curies is not None:
            logger.info('Annotation edges detected')
            logger.info('Annotate edge not currently supported')
            return message
        elif object_curies is not None:
            logger.info('Wildcard detected')
            for curie in object_curies:
                if object_category == 'biolink:Gene':
                    subjects = GeneToTissue.objects.filter(gene_id=curie)
                    #subjects = SpecificityMeanGene.objects.filter(gene_curie=curie).reverse()[0:10]
                else:
                    subjects = TissueToGene.objects.filter(tissue_id=curie)
                    #subjects = SpecificityMeanTissue.objects.filter(tissue_curie=curie).reverse()[0:30]
                if len(subjects) > 0:
                    logger.info('Found results for {}'.format(curie))
                    subject_curies = []
                    spec_vals = []
                    norm_spec_vals = []
                    p_vals = []
                    for subject in subjects:
                        subject_curie, spec_val, norm_spec_val, p_val = subject.get_result()
                        subject_curies.append(subject_curie)
                        spec_vals.append(spec_val)
                        norm_spec_vals.append(norm_spec_val)
                        p_vals.append(p_val)
                    node_binding_group, edge_binding_group = self._add_results(message, subject_mapping, qg_subject_id, subject_curies, subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, [curie], object_category, spec_vals, norm_spec_vals, p_vals)
                    node_bindings.extend(node_binding_group)
                    edge_bindings.extend(edge_binding_group)
        elif subject_curies is not None:
            logger.info('Wildcard detected')
            for curie in subject_curies:
                if subject_category == 'biolink:Gene':
                    objects = SpecificityMeanGene.objects.filter(gene_curie=curie).reverse()[0:10]
                else:
                    objects = SpecificityMeanTissue.objects.filter(tissue_curie=curie).reverse()[0:30]
                if len(objects) > 0:
                    logger.info('Found results for {}'.format(curie))
                    object_curies = []
                    spec_vals = []
                    norm_spec_vals = []
                    p_vals = []
                    for object in objects:
                        object_curie, spec_val, norm_spec_val, p_val = object.get_result()
                        object_curies.append(object_curie)
                        spec_vals.append(spec_val)
                        norm_spec_vals.append(norm_spec_val)
                        p_vals.append(p_val)
                    node_binding_group, edge_binding_group = self._add_results(message, subject_mapping, qg_subject_id, [curie], subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, object_curies, object_category, spec_vals, norm_spec_vals, p_vals)
                    node_bindings.extend(node_binding_group)
                    edge_bindings.extend(edge_binding_group)
        else:
            logger.info('No curies detected. Returning no results')
            return message
        results = Results(__root__ = parse_obj_as(HashableMapping, {}))
        for node_binding_dict, edge_binding_dict in zip(node_bindings, edge_bindings):
            analysis = Analysis(resource_id='infores:connections-hypothesis', edge_bindings = edge_binding_dict)
            result = Result(node_bindings = node_binding_dict, analyses=[analysis])
            results.add(result)
        message.results = results
        return message

