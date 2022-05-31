
'''trapi interface'''
import json
import pkgutil
from numpy import mean
from trapi_model.logger import Logger as TrapiLogger  # type: ignore
from trapi_model.meta_knowledge_graph import MetaKnowledgeGraph  # type: ignore
from trapi_model.query import Query  # type: ignore
from trapi_model.query_graph import QueryGraph  # type: ignore
from trapi_model.query_graph import QNode  # type: ignore
from trapi_model.query_graph import QEdge  # type: ignore
from trapi_model.meta_knowledge_graph import MetaNode, MetaEdge  # type: ignore
from chp_utils.curie_database import CurieDatabase  # type: ignore
from chp_utils.conflation import ConflationMap  # type: ignore
from . models import *
from .trapi_exceptions import *
from typing import List, Tuple


class TrapiInterface:
    # type: ignore #noqa
    def __init__(self, trapi_version: str = '1.2')
    self.trapi_version = trapi_version  # type: ignore #noqa

    def get_curies(self) -> CurieDatabase:
        return self._read_curies_file()

    def _read_curies_file(self) -> CurieDatabase:
        curies_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'app_meta_data/curies.json'
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
            'app_meta_data/meta_knowledge_graph.json'
        )  # type: ignore
        meta_kg_str = meta_kg_bytes.decode('utf-8')
        meta_kg_json = json.loads(meta_kg_str)
        meta_kg = MetaKnowledgeGraph.load(  # type: ignore
            self.trapi_version, None, meta_kg_json)  # type: ignore
        return meta_kg

    def _read_conflation_map(self) -> ConflationMap:
        conflation_map_bytes: bytes = pkgutil.get_data(
            'gene_specificity',
            'app_meta_data/conflation_map.json'
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
        # Get the edge object (there's only one)
        qedge: QEdge = query.message.query_graph.edges[0]  # type: ignore
        predicates = [predicate.get_curie() for predicate in qedge.predicates]  # type: ignore
        # Get q_subject and q_object nodes
        q_subject: QNode = query.message.query_graph.nodes[qedge.subject]  # type: ignore
        # type: ignore
        q_object: QNode = query.message.query_graph.nodes[qedge.object]  # type: ignore

        # determine if query is wildcard
        if self.is_wild_card(q_subject, q_object):
            mean_model, median_model = ModelFinder.find_model(q_subject, q_object, predicates)  # type: ignore
            if isinstance(mean_model, SpecificityMeanGene):
                mean_model.objects.filter(gene_curie=q_subject.ids[0])  # type: ignore
            else:
                mean_model: SpecificityMeanTissue
                mean_model.objects.filter(gene_curie=q_subject.ids[0])  # type: ignore
            if isinstance(median_model, SpecificityMedianGene):
                median_model.objects.filter(gene_curie=q_subject.ids[0])  # type: ignore
            else:
                median_model: SpecificityMedianTissue
                mean_model.objects.filter(gene_curie=q_subject.ids[0])  # type: ignore


    def is_wild_card(self, subject_node: QNode, object_node: QNode):  # type: ignore
        if subject_node.ids is None or object_node.ids is None:  # type: ignore
            return True
        return False

    def _reformat_biolink_term(self, biolink_term: str):
        return '_'.join(biolink_term.split(":"))


class ModelFinder:

    @staticmethod
    def find_model(qSubject: QNode, qObject: QNode, predicates: List[str]) -> Tuple(Model, Model):
        qSubject_categories = [category.get_curie() for category in qSubject.categories]  # type: ignore
        qObject_categories = [category.get_curie() for category in qObject.categories]  # type: ignore

        if "biolink:Gene" in qSubject_categories and\
            "biolink:GrossAnatomicalStructure" in qObject_categories and\
                "biolink:expressed_in" in predicates:
                return SpecificityMeanGene, SpecificityMedianGene

        elif "biolink:GrossAnatomicalStructure" in qSubject_categories and\
            "biolink:Gene" in qObject_categories and\
                "biolink:expresses" in predicates:
                return SpecificityMeanTissue, SpecificityMedianTissue
        raise NoSupportedQueriesFound
