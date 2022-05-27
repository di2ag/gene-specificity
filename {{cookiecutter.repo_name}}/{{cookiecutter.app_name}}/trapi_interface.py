'''trapi interface'''
import json # type: ignore #noqa
import pathlib

class TrapiInterface:
    def __init__(self, trapi_version={{ trapi_version }}): # type: ignore #noqa
        self.trapi_version = trapi_version

    def read_curies_file(): # type: ignore #noqa
        pathlib.Path(__file__).parent.resolve()
        pass
