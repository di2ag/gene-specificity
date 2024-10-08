from asyncio import constants
from gene_specificity.trapi_interface import TrapiInterface
from gene_specificity.apps import GeneSpecificityConfig
from reasoner_pydantic import MetaKnowledgeGraph, Message
from typing import TYPE_CHECKING, Union, List

def get_app_config(message: Union[Message, None]) -> GeneSpecificityConfig:
    return GeneSpecificityConfig


def get_trapi_interface(get_app_config: GeneSpecificityConfig = get_app_config(None)):
    return TrapiInterface(trapi_version='1.5')


def get_meta_knowledge_graph() -> MetaKnowledgeGraph:
    interface: TrapiInterface = get_trapi_interface()
    return interface.get_meta_knowledge_graph()


def get_response(consistent_queries: List[Message], logger):
    """ Should return app responses plus app_logs, status, and description information."""
    responses = []
    interface = get_trapi_interface()
    for consistent_query in consistent_queries:
        response = interface.get_response(consistent_query, logger)
        responses.append(response)
    return responses
