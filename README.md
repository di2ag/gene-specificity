# <ADD APP NAME HERE\>
<ADD APP DESCRIPTION HERE\>

## Trapi Transaction
Examples of the Trapi Query, Response, and Meta Knowledge Graph Objects that this app supports.

### Query
<!-- 
  create a query example for every supported query type in the meta knowledge graph for this app
  reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#query-
  -->
<details>
  <summary> Click to view json</summary>

  ```json
  {
    "message": {
      "query_graph": {
        "nodes": {
          "n0": {
            "ids": [
              "<ADD BIOLINK CURIE HERE>",
              "<ADD BIOLINK CURIE HERE>"
            ],
            "categories": [
              "<ADD BIOLINK ENTITY TYPE HERE>",
              "<ADD BIOLINK ENTITY TYPE HERE>"
            ],
            "is_set": <add boolean here>,
            "constraints": [
              {
                "id": "<ADD BIOLINK CURIE HERE>",
                "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
                "not": <add boolean here>,
                "operator": "<ADD AN OPERATOR HERE>",
                "value": [
                  "<ADD ATTRIBUTE VALUE HERE>",
                  "<ADD ATTRIBUTE VALUE HERE>"
                ],
                "unit_id": [
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>"
                ],
                "unit_name": [
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
                ]
              }
            ]
          },
          "n1": {
            "ids": [
              "<ADD BIOLINK CURIE HERE>",
              "<ADD BIOLINK CURIE HERE>"
            ],
            "categories": [
              "<ADD BIOLINK ENTITY TYPE HERE>",
              "<ADD BIOLINK ENTITY TYPE HERE>"
            ],
            "is_set": <add boolean here>,
            "constraints": [
              {
                "id": "<ADD BIOLINK CURIE HERE>",
                "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
                "not": <add boolean here>,
                "operator": "<ADD AN OPERATOR HERE>",
                "value": [
                  "<ADD ATTRIBUTE VALUE HERE>",
                  "<ADD ATTRIBUTE VALUE HERE>"
                ],
                "unit_id": [
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>"
                ],
                "unit_name": [
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
                ]
              }
            ]
          },
        },
        "edges": {
          "e0": {
            "predicates": [
              "<ADD BIOLINK PREDICATE HERE>",
              "<ADD BIOLINK PREDICATE HERE>"
            ],
            "subject": "n0",
            "object": "n1",
            "constraints": [
              {
                "id": "<ADD BIOLINK CURIE HERE>",
                "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
                "not": false,
                "operator": "<ADD AN OPERATOR HERE>",
                "value": [
                  "<ADD ATTRIBUTE VALUE HERE>",
                  "<ADD ATTRIBUTE VALUE HERE>"
                ],
                "unit_id": [
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                  "<ADD UNIT_ID FOR VALUE FIELD HERE>"
                ],
                "unit_name": [
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                  "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
                ]
              }
            ]
          }
        }
      },
      "knowledge_graph": {},
      "results": {}
    }
  }
  ```
</details>

### Response
<!-- 
  create a response example for every supported query type in the meta knowledge graph for this app
  reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#response-
 -->
<details>
  <summary> click to view json example </summary>

```json
{
  "message": {
    "query_graph": {
      "nodes": {
        "n0": {
          "ids": [
            "<ADD BIOLINK CURIE HERE>",
            "<ADD BIOLINK CURIE HERE>"
          ],
          "categories": [
            "<ADD BIOLINK ENTITY TYPE HERE>",
            "<ADD BIOLINK ENTITY TYPE HERE>"
          ],
          "is_set": <add boolean here>,
          "constraints": [
            {
              "id": "<ADD BIOLINK CURIE HERE>",
              "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
              "not": <add boolean here>,
              "operator": "<ADD AN OPERATOR HERE>",
              "value": [
                "<ADD ATTRIBUTE VALUE HERE>",
                "<ADD ATTRIBUTE VALUE HERE>"
              ],
              "unit_id": [
                "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                "<ADD UNIT_ID FOR VALUE FIELD HERE>"
              ],
              "unit_name": [
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
              ]
            }
          ]
        },
        "n1": {
          "ids": [
            "<ADD BIOLINK CURIE HERE>",
            "<ADD BIOLINK CURIE HERE>"
          ],
          "categories": [
            "<ADD BIOLINK ENTITY TYPE HERE>",
            "<ADD BIOLINK ENTITY TYPE HERE>"
          ],
          "is_set": <add boolean here>,
          "constraints": [
            {
              "id": "<ADD BIOLINK CURIE HERE>",
              "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
              "not": <add boolean here>,
              "operator": "<ADD AN OPERATOR HERE>",
              "value": [
                "<ADD ATTRIBUTE VALUE HERE>",
                "<ADD ATTRIBUTE VALUE HERE>"
              ],
              "unit_id": [
                "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                "<ADD UNIT_ID FOR VALUE FIELD HERE>"
              ],
              "unit_name": [
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
              ]
            }
          ]
        },
      },
      "edges": {
        "e0": {
          "predicates": [
            "<ADD BIOLINK PREDICATE HERE>",
            "<ADD BIOLINK PREDICATE HERE>"
          ],
          "subject": "n0",
          "object": "n1",
          "constraints": [
            {
              "id": "<ADD BIOLINK CURIE HERE>",
              "name": "<ADD HUMAN READABLE NAME FOR THE ID HERE>",
              "not": false,
              "operator": "<ADD AN OPERATOR HERE>",
              "value": [
                "<ADD ATTRIBUTE VALUE HERE>",
                "<ADD ATTRIBUTE VALUE HERE>"
              ],
              "unit_id": [
                "<ADD UNIT_ID FOR VALUE FIELD HERE>",
                "<ADD UNIT_ID FOR VALUE FIELD HERE>"
              ],
              "unit_name": [
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>",
                "<ADD HUMAN READABLE NAME FOR THE VALUE FIELD HERE>"
              ]
            }
          ]
        }
      }
    },
    "knowledge_graph": {
      "nodes": {
        "name": "<ADD BIOLINK ENTITY NAME HERE>",
        "categories": [
          "<ADD BIOLINK ENTITY TYPE HERE>",
          "<ADD BIOLINK ENTITY TYPE HERE>"
        ],
        "attributes": [
          {
            "attribute_type_id": "<ADD BIOLINK CURIE HERE>",
            "original_attribute_name": "<ADD TERM USED BY ORIGINAL SOURCE HERE>",
            "value": "<ADD ATTRIBUTE VALUE HERE>",
            "value_type_id": "<ADD BIOLINK CURIE HERE>",
            "attribute_source": "<ADD ATTRIBUTE SOURCE HERE>",
            "value_url": "<ADD URL TO ADDITIONAL DOCUMENTATION FOR THIS VALUE>",
            "description": "<ADD DESCRIPTION HERE>",
            "attributes": [
              {
                "attribute_type_id": "<ADD BIOLINK CURIE HERE>",
                "original_attribute_name": "<ADD TERM USED BY ORIGINAL SOURCE HERE>",
                "value": "<ADD ATTRIBUTE VALUE HERE>",
                "value_type_id": "<ADD BIOLINK CURIE HERE>",
                "attribute_source": "<ADD ATTRIBUTE SOURCE HERE>",
                "value_url": "<ADD URL TO ADDITIONAL DOCUMENTATION FOR THIS VALUE>",
                "description": "<ADD DESCRIPTION HERE>",
              }
            ]
          }
        ]
      },
      "edges": {
        "e0": {
          "predicate": "<ADD PREDICATE HERE>",
          "subject": "n0",
          "object": "n1",
          "attributes": [
            {
              "attribute_type_id": "<ADD BIOLINK CURIE HERE>",
              "original_attribute_name": "<ADD TERM USED BY ORIGINAL SOURCE HERE>",
              "value": "<ADD ATTRIBUTE VALUE HERE>",
              "value_type_id": "<ADD BIOLINK CURIE HERE>",
              "attribute_source": "<ADD ATTRIBUTE SOURCE HERE>",
              "value_url": "<ADD URL TO ADDITIONAL DOCUMENTATION FOR THIS VALUE>",
              "description": "<ADD DESCRIPTION HERE>",
              "attributes": [
                {
                  "attribute_type_id": "<ADD BIOLINK CURIE HERE>",
                  "original_attribute_name": "<ADD TERM USED BY ORIGINAL SOURCE HERE>",
                  "value": "<ADD ATTRIBUTE VALUE HERE>",
                  "value_type_id": "<ADD BIOLINK CURIE HERE>",
                  "attribute_source": "<ADD ATTRIBUTE SOURCE HERE>",
                  "value_url": "<ADD URL TO ADDITIONAL DOCUMENTATION FOR THIS VALUE>",
                  "description": "<ADD DESCRIPTION HERE>",
                }
              ]
            }
          ]
        }
      }
    },
    "results": [
      {
        "node_bindings": {
          "n0": [
            {
              "id": "<ADD NODE CURIE HERE>"
            }
          ],
          "n1": [
            {
              "id": "<ADD NODE CURIE HERE>"
            }
          ]
        },
        "edge_bindings": {
          "e1": [
            {
              "id": "<ADD EDGE ID HERE>"
            }
          ]
        },
        "score": 0
      },
    ]
  },
  "logs": [],
  "workflow": [
    {
      "id": "<ADD WORKFLOW TYPE HERE>"
    }
  ]
}
```
</details>

### Meta Knowledge Graph
<!-- 
  create a meta knowledge graph example the app
  reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#response-
 -->
<details>
  <summary> Click to view json example </summary>

```json
{
  "nodes": [
    {
      "<ADD BIOLINK ENTITY TYPE HERE>": {
        "id_prefixes":[
          "<ADD BIOLINK ENTITY TYPE HERE>",
          "<ADD BIOLINK ENTITY TYPE HERE>"
        ],
        "attributes": [
          {
            "attribute_type_id": "",
            "attribute_source": "",
            "original_attribute_names": [
              "<ADD META ATTRIBUTE NAME HERE>",
              "<ADD META ATTRIBUTE NAME HERE>"
            ],
            "constraint_use": <add boolean here>,
            "constraint_name": "<ADD CONSTRAINT NAME HERE>" 
          }
        ]
      },
    }
  ],
  "edges": [
    {
      "subject": "<ADD SUBJECT CATEGORY HERE>",
      "object": "<ADD OBJECT CATEGORY HERE",
      "predicate": "<ADD PREDICATE HERE>",
      "attributes": [
        {
          "attribute_type_id": "<ADD ATTRIBUTE CURIE HERE>",
          "attribute_source": "<ADD ATTRIBUTE SOURCE HERE>",
          "original_attribute_names": [
            "<ADD META ATTRIBUTE NAME HERE>",
            "<ADD META ATTRIBUTE NAME HERE>"
          ],
          "constraint_use": <add boolean here>,
          "constraint_name": "<ADD CONSTRAINT NAME HERE>" 
        }
      ]
    }
  ]
}
```
</details>

## References
### Example Reference 1
  <!-- use \ to indicate a linebreak -->
  <!-- link to the reference website -->
  Link: [<ADD LINK TO REFERENCE HERE\>](www.example.com)\
  Description: <ADD DESCRIPTION FOR REFERENCE 2 HERE>

### Example Reference 2
  <!-- use \ to indicate a linebreak -->
  <!-- if no website is available to link to, just name it like so -->
  Name: <ADD REFERENCE WITH NO WEBSITE\>\
  Description: <ADD DESCRIPTION FOR REFERENCE 2 HERE>