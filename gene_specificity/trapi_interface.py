'''trapi interface'''
import uuid
import json
import pkgutil
import logging
from typing import Tuple, Union
from django.db.models import QuerySet
from reasoner_pydantic import MetaKnowledgeGraph, Message, KnowledgeGraph
from reasoner_pydantic.kgraph import RetrievalSource, Attribute
from reasoner_pydantic.results import NodeBinding, EdgeBinding, Result, Results, Analysis
from gene_specificity.models import SpecificityMeanGene, SpecificityMeanTissue, CurieTemplate, CurieTemplateMatch

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

    def _get_attributes(self, val):
        att_1 = Attribute(attribute_type_id = 'Specificity',
                          value_type_id='biolink:has_evidence',
                          value=val,
                          description="Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.")
        att_2 = Attribute(attribute_type_id = 'primary_knowledge_source',
                          value='infores:connections-hypothesis',
                          value_url='https://github.com/di2ag/gene-specificity',
                          description='The Connections Hypothesis Provider from NCATS Translator')
        return {att_1, att_2}

    def _add_results(self, message, subject_mapping, qg_subject_id, subject_curies, subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, object_curies, object_category, vals):
        nodes = dict()
        edges = dict()
        results = set()
        val_id = 0
        for subject_curie in subject_curies:
            for object_curie in object_curies:
                nodes[subject_curie] = {"categories": [subject_category]}
                nodes[object_curie] = {"categories": [object_category]}
                kg_edge_id = str(uuid.uuid4())
                edges[kg_edge_id] = {"predicate": predicate,
                                     "subject": subject_curie,
                                     "object": object_curie,
                                     "sources": self._get_sources(),
                                     "attributes": self._get_attributes(vals[val_id])}
                val_id += 1
                node_bindings = dict()
                if subject_curie in subject_mapping:
                    node_bindings[qg_subject_id] = {NodeBinding(id = subject_curie, query_id = subject_mapping[subject_curie])}
                else:
                    node_bindings[qg_subject_id] = {NodeBinding(id = subject_curie)}
                if object_curie in object_mapping:
                    node_bindings[qg_object_id] = {NodeBinding(id = object_curie, query_id = object_mapping[object_curie])}
                else:
                    node_bindings[qg_object_id] = {NodeBinding(id = object_curie)}
                edge_bindings = dict()
                edge_bindings[qg_edge_id] = {EdgeBinding(id = kg_edge_id)}
                analysis = Analysis(resource_id='infores:connections-hypothesis', edge_bindings=edge_bindings)
                result = Result(node_bindings=node_bindings, analyses=[analysis])
                results.add(result)
        kgraph = KnowledgeGraph(nodes=nodes, edges=edges)
        rgraph = Results(__root__=results)
        if message.knowledge_graph is not None:
            message.knowledge_graph.update(kgraph)
        else:
	        message.knowledge_graph = kgraph
        if message.results is not None:
            message.results.update(rgraph)
        else:
            message.results=rgraph

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
        threshold = 10
        if subject_curies is not None and object_curies is not None:
            logger.info('Annotation edges detected')
            logger.info('Annotate edge not currently supported')
        elif object_curies is not None:
            logger.info('Wildcard detected')
            for curie in object_curies:
                if object_category == 'biolink:Gene':
                    subjects = SpecificityMeanGene.objects.filter(gene_curie=curie).reverse()[:threshold]
                else:
                    subjects = SpecificityMeanTissue.objects.filter(tissue_curie=curie).reverse()[:threshold]
                if len(subjects) > 0:
                    logger.info('Found results for {}'.format(curie))
                    subject_curies = [subject.get_result()[0] for subject in subjects]
                    vals = [subject.get_result()[2] for subject in subjects]
                    self._add_results(message, subject_mapping, qg_subject_id, subject_curies, subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, [curie], object_category, vals)
        elif subject_curies is not None:
            logger.info('Wildcard detected')
            for curie in subject_curies:
                if subject_category == 'biolink:Gene':
                    objects = SpecificityMeanGene.objects.filter(gene_curie=curie).reverse()[:threshold]
                else:
                    objects = SpecificityMeanTissue.objects.filter(tissue_curie=curie).reverse()[:threshold]
                if len(objects) > 0:
                    logger.info('Found results for {}'.format(curie))
                    object_curies = [object.get_result()[0] for object in objects]
                    vals = [object.get_result()[2] for object in objects]
                    self._add_results(message, subject_mapping, qg_subject_id, [curie], subject_category, predicate, qg_edge_id, object_mapping, qg_object_id, object_curies, object_category, vals)
        else:
            logger.info('No curies detected. Returning no results')

        return message
