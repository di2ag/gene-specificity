'''trapi interface'''
import uuid
import json
import pkgutil
import logging
from typing import Tuple, Union
from django.db.models import QuerySet
from reasoner_pydantic import MetaKnowledgeGraph, Message, KnowledgeGraph
from reasoner_pydantic.kgraph import RetrievalSource, Attribute
from reasoner_pydantic.results import NodeBinding, Result, Results
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

    def _add_results(self, message, qg_subject_id, subject_curies, subject_category, predicate, qg_object_id, object_curies, object_category, vals):
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
                node_bindings[qg_subject_id] = {NodeBinding(id = subject_curie)}
                node_bindings[qg_object_id] = {NodeBinding(id = object_curie)}
                result = Result(node_bindings=node_bindings)
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
                    print(match.curie)
                    descendant_curies.add(match.curie)
                    if id != match.curie:
                        print("made mapping")
                        mapping[match.curie] = id
            return mapping, list(descendant_curies), category
        return dict(), None, category

    def get_response(self, message: Message, logger):
        print(message.to_dict())
        for edge_id, edge in message.query_graph.edges.items():
            predicate = edge.predicates[0]
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
                    print(curie)
                    logger.info('Found results for {}'.format(curie))
                    subject_curies = [subject.get_result()[0] for subject in subjects]
                    vals = [subject.get_result()[2] for subject in subjects]
                    self._add_results(message, qg_subject_id, subject_curies, subject_category, predicate, qg_object_id, [curie], object_category, vals)
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
                    self._add_results(message, qg_subject_id, [curie], subject_category, predicate, qg_object_id, object_curies, object_category, vals)
        else:
            logger.info('No curies detected. Returning no results')

        return message

        '''
        # Get the edge object (there's only one)
        qedges: QEdge = query.message.query_graph.edges  # type: ignore
        edge_id = list(qedges.keys())[0]
        qedge: QEdge = qedges[edge_id]  # type: ignore
        predicates = [predicate.get_curie()
                      for predicate in qedge.predicates]  # type: ignore

        # Get q_subject and q_object nodes
        q_subject_node: QNode = query.message.query_graph.nodes[qedge.subject]
        q_object_node: QNode = query.message.query_graph.nodes[qedge.object]

        qSubject_categories = [category.get_curie()
                               for category in q_subject_node.categories]  # type: ignore
        qObject_categories = [category.get_curie()
                              for category in q_object_node.categories]  # type: ignore

        if not self.is_wild_card(q_subject_node, q_object_node):
            return self._return_no_result(query, 'gene_specificity app can not handle curie formation. App only supports fill operation')

        # if true then subject node is the fill node
        if q_subject_node.ids is None:
            curie = q_object_node.ids[0]
            subject_wildcard = True
            if curie not in self.get_curies().to_dict()[q_object_node.categories[0].get_curie()]:
                return self._return_no_result(query, '{} curie not supported in gene_specificity app'.format(curie))
        # else object node is fill
        else:
            curie = q_subject_node.ids[0]
            subject_wildcard=False
            if curie not in self.get_curies().to_dict()[q_subject_node.categories[0].get_curie()]:
                return self._return_no_result(query, '{} curie not supported in gene_specificity app'.format(curie))


        # TODO: this if statement is a temp fix due to an error in the data
        if "ENSEMBL" in curie:
            curie = curie.split(':')[1]

        # determine if query is wildcard
        if "biolink:Gene" in qSubject_categories and\
            "biolink:GrossAnatomicalStructure" in qObject_categories and\
                "biolink:expressed_in" in predicates:
            if subject_wildcard:
                results: QuerySet = SpecificityMeanTissue.objects.filter(
                    tissue_curie=curie).reverse()
            else:
                results: QuerySet = SpecificityMeanGene.objects.filter(
                    gene_curie=curie).reverse()
        elif "biolink:GrossAnatomicalStructure" in qSubject_categories and\
            "biolink:Gene" in qObject_categories and\
                "biolink:expresses" in predicates:
            if subject_wildcard:
                results: QuerySet = SpecificityMeanGene.objects.filter(
                    gene_curie=curie).reverse()
            else:
                results: QuerySet = SpecificityMeanTissue.objects.filter(
                    tissue_curie=curie).reverse()
        else:
            return self._return_no_result(query, 'gene_specificity app can not handle curie formation. App only supports fill operation')

        # type: ignore
        #max_results = query.max_results
        #if max_results is not None:
        results = results[:10]  # type: ignore
        return self._build_response(query, q_subject_node, q_object_node, subject_wildcard, results, response_object)
        '''

    '''
    def _build_response(self, query: Query, q_subject_node: QNode, q_object_node: QNode, subject_wildcard: bool, data_base_results: QuerySet, response_object: Query):
        response_results = query.message.results

        logs = query.logger.to_dict()
        ontological_conflate_term = None
        if len(logs) > 0:
            for log_dict in logs:
                info_message = log_dict['message']
                if 'Ontologically expanded' in info_message:
                    ontological_conflate_term = info_message.split(' ')[2]

        knowledge_graph = query.message.knowledge_graph
        # add non_fill node to kg
        if subject_wildcard:
            curie = q_object_node.ids[0].split(':')
            if 'ENSG' in curie:
                curie = curie.split(':')
            non_fill_node_name: str = self.get_curies().to_dict()[q_object_node.categories[0].get_curie()][q_object_node.ids[0]][0]
            non_fill_node_curie: str = knowledge_graph.add_node(q_object_node.ids[0], non_fill_node_name, q_object_node.categories[0].get_curie())
            fill_node = q_subject_node
            non_fill_node = q_object_node
        else:
            curie = q_subject_node.ids[0].split(':')
            if 'ENSG' in curie:
                curie = curie.split(':')
            non_fill_node_name: str = self.get_curies().to_dict()[q_subject_node.categories[0].get_curie()][q_subject_node.ids[0]][0]
            non_fill_node_curie: str = knowledge_graph.add_node(q_subject_node.ids[0], non_fill_node_name, q_subject_node.categories[0].get_curie())
            fill_node = q_object_node
            non_fill_node = q_subject_node

        for k, v in query.message.query_graph.nodes.items():
            if v == non_fill_node:
                non_fill_key = k
            elif v == fill_node:
                fill_key = k

        for result in data_base_results:  # type: ignore

            # type: ignore
            result: Tuple[str, str, float] = result.get_result()  # type: ignore

            if 'ENSG' in result[0] and result[2] < 1: #threshold
                continue
            node_bindings = {}
            edge_bindings = {}

            node_bindings.update({non_fill_key: {'ids' : [non_fill_node_curie],
                                                 'query_id' : ontological_conflate_term}})

            fill_id = result[0]
            fill_categories = result[1]
            specificity_mean = result[2]
            if 'ENSG' in fill_id:
                fill_id = 'ENSEMBL:'+fill_id
            fill_name: str = self.get_curies().to_dict()[fill_categories][fill_id][0]  # type: ignore
            fill_node_curie: str = knowledge_graph.add_node(
                fill_id, fill_name, fill_categories)  # type: ignore

            node_bindings.update(
                {fill_key: [fill_node_curie]})  # type: ignore

            subject_categories = [category.get_curie()
                        for category in q_subject_node.categories]  # type: ignore
            predicate_str: str = ''
            if "biolink:GrossAnatomicalStructure" in subject_categories:  # type: ignore
                predicate_str = "biolink:expresses"
            else:
                predicate_str = "biolink:expressed_in"

            s_1 = Source(
                trapi_version = self.trapi_version,
                biolink_version = None,
                resource_id='infores:connections-hypothesis',
                resource_role='primary_knowledge_source',
                description='The Connections Hypothesis Provider from NCATS Translator.',
            )
            s_2 = Source(
                trapi_version = self.trapi_version,
                biolink_version = None,
                resource_id='infores:gtex',
                resource_role='supporting_data_source',
                description='The Genotype-Tissue Expression (GTEx) project'
            )
            sources = [s_1, s_2]


            if subject_wildcard:
                kedge_key: KEdge = knowledge_graph.add_edge(  # type: ignore
                    k_subject=fill_node_curie,
                    k_object=non_fill_node_curie,
                    sources=sources,
                    predicate=predicate_str,)
            else:
                kedge_key: KEdge = knowledge_graph.add_edge(  # type: ignore
                    k_subject=non_fill_node_curie,
                    k_object=fill_node_curie,
                    sources=sources,
                    predicate=predicate_str)

            qedge_key = list(query.message.query_graph.edges.keys())[0]  # type: ignore
            edge_bindings.update({qedge_key: [kedge_key]})  # type: ignore
            response_results.add_result(node_bindings, edge_bindings)
            kedge: KEdge = knowledge_graph.edges[kedge_key]

            # add specificity
            kedge.add_attribute(
                attribute_type_id="Specificity",
                original_attribute_name=None,
                value=specificity_mean,
                value_type_id="biolink:has_evidence",
                attribute_source=None,
                value_url=None,
                description="Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity."
            )

            # add epc
            kedge.add_attribute(
                attribute_type_id="primary_knowledge_source",
                original_attribute_name=None,
                value="infores:connections-hypothesis",
                value_type_id="biolink:InformationResource",
                attribute_source="infores:connections-hypothesis",
                value_url="https://github.com/di2ag/gene-specificity",
                description="The Connections Hypothesis Provider from NCATS Translator.",
            )

        # response_object: Query = copy(query)

        response_object.message.results = response_results
        response_object.message.knowledge_graph = knowledge_graph
        return response_object

    def is_wild_card(self, subject_node: QNode, object_node: QNode):  # type: ignore
        if subject_node.ids is None and object_node.ids is not None:  # type: ignore
            return True
        elif subject_node.ids is not None and object_node.ids is None:
            return True
        return False

    def _reformat_biolink_term(self, biolink_term: str):
        return '_'.join(biolink_term.split(":"))

    '''
