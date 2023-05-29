import json
import requests

def query_ontology_kp(curies, category):
    query_graph = {
        "nodes": {
            "n0": {
                "ids": curies
            },
            "n1": {
                "categories": [category]
            },
        },
        "edges": {
            "e0": {
                "subject": "n1",
                "object": "n0",
                "predicates": ["biolink:part_of", "biolink:subclass_of"],
                "attribute_constraints": [
                    {
                     "id": "EDAM-DATA:2589",
                     "name": "hierarchy",
                     "operator": "==",
                     "value": "direct"
                    }
                ]
            }
        }
    }
    # Wrap in a message and in a query
    query = {
        "message": {
            "query_graph": query_graph,
        }
    }
    url = 'https://ontology-kp.apps.renci.org/query'
    r = requests.post(url, json=query, timeout=1000)
    answer = json.loads(r.content)
    mapping = dict()
    descendant_curies = []
    for edge_id, edge in answer['message']['knowledge_graph']['edges'].items():
        subject = edge['subject']
        object = edge['object']
        mapping[subject] = object
        descendant_curies.append(subject)
    return mapping, descendant_curies


def get_curie_descendant_mapping(qnode):
    ids = qnode.ids
    category = qnode.categories[0]
    if ids is not None:
        ids = list(ids)
        mapping, descendant_curies = query_ontology_kp(ids, category)
        ids.extend(descendant_curies)
        return mapping, ids, category
    return dict(), None, category
