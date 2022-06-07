from gene_specificity.trapi_interface import TrapiInterface
# from .apps import {{cookiecutter.app_config_name}}  # type: ignore #noqa
from gene_specificity.apps import GeneSpecificityConfig
from trapi_model.knowledge_graph import KnowledgeGraph  # type: ignore #noqa
from trapi_model.meta_knowledge_graph import MetaKnowledgeGraph  # type: ignore #noqa
from chp_utils.curie_database import CurieDatabase  # type: ignore #noqa
from chp_utils.conflation import ConflationMap  # type: ignore #noqa
from typing import TYPE_CHECKING, Union, List
from trapi_model.query import Query # type: ignore #noqa


def get_app_config(query: Union[Query, None]) -> GeneSpecificityConfig:
    return GeneSpecificityConfig  # type: ignore


def get_trapi_interface(get_app_config: GeneSpecificityConfig = get_app_config(None)):
    return TrapiInterface(trapi_version='1.2')


def get_meta_knowledge_graph() -> MetaKnowledgeGraph:
    interface: TrapiInterface = get_trapi_interface()
    return interface.get_meta_knowledge_graph()


def get_curies() -> CurieDatabase:
    interface = get_trapi_interface()
    return interface.get_curies()


def get_conflation_map() -> ConflationMap:
    interface = get_trapi_interface()
    return interface.get_conflation_map()


def get_response(consistent_queries: List[Query]):  # type: ignore
    """ Should return app responses plus app_logs, status, and description information."""
    responses = []
    status: str = None  # type: ignore #noqa
    description: str = None  # type: ignore #noqa
    app_logs = []
    if isinstance(consistent_queries, list):
        for consistent_query in consistent_queries:  # type: ignore #noqa
            interface = get_trapi_interface()
            response = interface.get_response(consistent_query)  # type: ignore
            responses.append(response)  # type: ignore
            app_logs.extend(interface.logger.to_dict())  # type: ignore
    else:
        interface = get_trapi_interface()
        response = interface.get_response(consistent_queries)  # type: ignore
        responses.append(response)  # type: ignore
        app_logs.extend(interface.logger.to_dict())  # type: ignore
    status = 'Success'
    return responses, app_logs, status, description  # type: ignore
