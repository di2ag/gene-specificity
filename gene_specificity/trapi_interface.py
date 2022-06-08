
'''trapi interface'''
from copy import copy
import json
import pkgutil
from typing import Tuple, Union

from django.db.models import QuerySet

from chp_utils.conflation import ConflationMap  # type: ignore
from chp_utils.curie_database import CurieDatabase  # type: ignore
from trapi_model.logger import Logger as TrapiLogger
from trapi_model.meta_knowledge_graph import MetaKnowledgeGraph  # type: ignore
from trapi_model.query import Query  # type: ignore
from trapi_model.query_graph import QEdge  # type: ignore
from trapi_model.query_graph import QNode  # type: ignore
from trapi_model.knowledge_graph import KEdge, KNode

from gene_specificity.models import SpecificityMeanGene, SpecificityMeanTissue
from gene_specificity.trapi_exceptions import NoSupportedQueriesFound


class TrapiInterface:
    # type: ignore #noqa
    def __init__(self, trapi_version: str = '1.2'):
        self.trapi_version = trapi_version  # type: ignore #noqa
        # Initialize interface level logger
        self.logger = TrapiLogger()

    def get_curies(self) -> CurieDatabase:
        return self._read_curies_file()

    def _read_curies_file(self) -> CurieDatabase:
        curies_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'gene_specificity/app_meta_data/curies.json'
        )  # type: ignore
        curies_str = curies_bytes.decode('utf-8')
        curies_json = json.loads(curies_str)
        curies = CurieDatabase(curies_json)
        return curies

    def get_meta_knowledge_graph(self) -> MetaKnowledgeGraph:
        return self._read_meta_knowledge_graph()

    def _read_meta_knowledge_graph(self) -> MetaKnowledgeGraph:
        meta_kg_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'gene_specificity/app_meta_data/meta_knowledge_graph.json'
        )  # type: ignore
        meta_kg_str = meta_kg_bytes.decode('utf-8')
        meta_kg_json = json.loads(meta_kg_str)
        meta_kg = MetaKnowledgeGraph.load(  # type: ignore
            self.trapi_version, None, meta_kg_json)  # type: ignore
        return meta_kg

    def _read_conflation_map(self) -> ConflationMap:
        conflation_map_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'gene_specificity/app_meta_data/conflation_map.json'
        )  # type: ignore
        conflation_map_str = conflation_map_bytes.decode('utf-8')
        conflation_map_json = json.loads(conflation_map_str)
        conflation_map = ConflationMap(conflation_map_json)
        return conflation_map

    def get_conflation_map(self) -> ConflationMap:
        return self._read_conflation_map()

    def get_name(self) -> str:
        return 'gene_specificity'

    def get_response(self, query: Query):  # type: ignore
        response_object: Query = query.get_copy()

        # Get the edge object (there's only one)
        qedges: QEdge = query.message.query_graph.edges  # type: ignore
        qedge: QEdge = qedges['e0']  # type: ignore
        predicates = [predicate.get_curie()
                      for predicate in qedge.predicates]  # type: ignore
        # Get q_subject and q_object nodes
        # type: ignore
        q_subject_node: QNode = query.message.query_graph.nodes[qedge.subject]
        q_subject_id: str = q_subject_node.ids[0]  # type: ignore

        # TODO: this if statement is a temp fix due to an error in the data
        if "ENSEMBL" in q_subject_id:
            q_subject_id = q_subject_id.split(':')[1]

        # type: ignore
        q_object: QNode = query.message.query_graph.nodes[qedge.object]

        qSubject_categories = [category.get_curie()
                               for category in q_subject_node.categories]  # type: ignore
        qObject_categories = [category.get_curie()
                              for category in q_object.categories]  # type: ignore

        # determine if query is wildcard
        if self.is_wild_card(q_subject_node, q_object):
            if "biolink:Gene" in qSubject_categories and\
                "biolink:GrossAnatomicalStructure" in qObject_categories and\
                    "biolink:expressed_in" in predicates:
                results: QuerySet = SpecificityMeanGene.objects.filter(
                    gene_curie=q_subject_id).reverse()
            elif "biolink:GrossAnatomicalStructure" in qSubject_categories and\
                "biolink:Gene" in qObject_categories and\
                    "biolink:expresses" in predicates:
                results: QuerySet = SpecificityMeanTissue.objects.filter(
                    tissue_curie=q_subject_id).reverse()
            else:
                raise NoSupportedQueriesFound
        # type: ignore
        max_results = query.max_results
        if max_results is not None:
            results = results[:max_results]  # type: ignore
        return self._build_response(query, q_subject_node, results, response_object)  # type: ignore

    def _build_response(self, query: Query, q_subject_node: QNode, data_base_results: QuerySet, response_object: Query):
        response_results = query.message.results
        node_bindings = {}
        edge_bindings = {}

        knowledge_graph = query.message.knowledge_graph
        # add the subject from the query graph
        subject_name: str = self.get_curies().to_dict(
        )[q_subject_node.categories[0].get_curie()][q_subject_node.ids[0]][0]  # type: ignore

        knode_subject_curie: str = knowledge_graph.add_node(
            q_subject_node.ids[0], subject_name, q_subject_node.categories[0].get_curie())  # type: ignore

        for k, v in query.message.query_graph.nodes.items():
            if v == q_subject_node:
                subject_key = k
                break

        node_bindings.update({subject_key: [knode_subject_curie]})  # type: ignore

        qnode: QNode
        for qnode in query.message.query_graph.nodes:
            qnode = query.message.query_graph.nodes[qnode]
            if qnode != q_subject_node:
                wildcard_node_key = query.message.query_graph.find_nodes(  # type: ignore
                    qnode.categories)[0]
        for result in data_base_results:  # type: ignore
            # type: ignore
            result: Tuple[str, str, float] = result.get_result()  # type: ignore
            object_id = result[0]
            object_categories = result[1]
            specificity_mean = result[2]

            object_name: str = self.get_curies().to_dict(
            )[object_categories][object_id][0]  # type: ignore
            knode_object_curie: str = knowledge_graph.add_node(
                object_id, object_name, object_categories)  # type: ignore
            
            node_bindings.update(
                {wildcard_node_key: [knode_object_curie]})  # type: ignore

            subject_categories = [category.get_curie()
                        for category in q_subject_node.categories]  # type: ignore
            predicate_str: str = ''
            if "biolink:GrossAnatomicalStructure" in subject_categories:  # type: ignore
                predicate_str = "biolink:expressed_in"
            else:
                predicate_str = "biolink:expresses"
            kedge_key: KEdge = knowledge_graph.add_edge(  # type: ignore
                k_subject=knode_subject_curie,
                k_object=knode_object_curie,
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
                description="Specificity value between a tissue and gene indicates a gene's RNA\
                    Sequence expression specificity to that tissue. Values closer to 0 indicate no\
                        expression specificity and values closer to 5.755 or log_2(54) (54 being\
                            the number of tissues used in this analysis) indicate complete\
                                specificity."
            )

            # add epc
            kedge.add_attribute(
                attribute_type_id="primary_knowledge_source",
                original_attribute_name=None,
                value="infores:connections-hypothesis",
                value_type_id="biolink:InformationResource",
                attribute_source="infores:connections-hypothesis",
                value_url="http://chp.thayer.dartmouth.edu",
                description="The Connections Hypothesis Provider from NCATS Translator.",
            )

            kedge.add_attribute(
                attribute_type_id="biolink:support_data_source",
                original_attribute_name=None,
                value="infores:tcga",
                value_type_id="biolink:InformationResource",
                attribute_source="infores:gdc",
                value_url="https://gtexportal.org/home/",
                description="The Cancer Genome Atlas provided by the GDC Data Portal."
            )


        # response_object: Query = copy(query)

        response_object.message.results = response_results
        response_object.message.knowledge_graph = knowledge_graph
        return response_object

    def is_wild_card(self, subject_node: QNode, object_node: QNode):  # type: ignore
        if subject_node.ids is None or object_node.ids is None:  # type: ignore
            return True
        return False

    def _reformat_biolink_term(self, biolink_term: str):
        return '_'.join(biolink_term.split(":"))
