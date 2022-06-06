# Gene Specificity Index
The Gene Specificity Index exposes a rank ordering over gene-tissue RNA Sequence relationships. Genes that have a high expression and express only in a small subset of tissues will be ranked higher than genes that have a lower expression and express in many tissue types. We build the Gene Specificity Index using data from the [Genotype-Tissue Expression (GTEx) project](#gtex). GTEx exposes RNA Sequence data expression from samples over a large range of tissues (54). We use the gene expression values of these samples to build tissue specific profiles that can be used to compare. The methodology is taken from [Defining diversity, specialization, and gene specificity in transcriptomes through information theory](#defining-diversity-specialization-and-gene-specificity-in-transcriptomes-through-information-theory) by Octavio Martínez and M. Humberto Reyes-Valdés. Specificity values range from 0 to 5.755 (log<sub>2</sub>(x), where x is the number of tissues) where values closer to 0 indicate no specificity and values closer to 5.755 indicicate complete specificity

## Trapi Transaction
Examples of the Trapi Query, Response, and Meta Knowledge Graph Objects that this app supports.

### Query
<!-- 
  create a query example for every supported query type in the meta knowledge graph for this app
  reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#query-
  -->
<details>
  <summary> Click to view json example</summary>

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
  <summary> Click to view json example</summary>

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
        "score": <ADD SCORE HERE>
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
### GTEx
  <!-- use \ to indicate a linebreak -->
  <!-- link to the reference website -->
  Link: <https://gtexportal.org/home/>\
  Description: The Genotype-Tissue Expression (GTEx) project is an ongoing effort to build a comprehensive public resource to study tissue-specific gene expression and regulation. Samples were collected from 54 non-diseased tissue sites across nearly 1000 individuals, primarily for molecular assays including WGS, WES, and RNA-Seq. Remaining samples are available from the GTEx Biobank. The GTEx Portal provides open access to data including gene expression, QTLs, and histology images.

### Defining diversity, specialization, and gene specificity in transcriptomes through information theory
  <!-- use \ to indicate a linebreak -->
  <!-- if no website is available to link to, just name it like so -->
  Link: <https://www.pnas.org/doi/10.1073/pnas.0803479105>\
  Abstract: The transcriptome is a set of genes transcribed in a given tissue under specific conditions and can be characterized by a list of genes with their corresponding frequencies of transcription. Transcriptome changes can be measured by counting gene tags from mRNA libraries or by measuring light signals in DNA microarrays. In any case, it is difficult to completely comprehend the global changes that occur in the transcriptome, given that thousands of gene expression measurements are involved. We propose an approach to define and estimate the diversity and specialization of transcriptomes and gene specificity. We define transcriptome diversity as the Shannon entropy of its frequency distribution. Gene specificity is defined as the mutual information between the tissues and the corresponding transcript, allowing detection of either housekeeping or highly specific genes and clarifying the meaning of these concepts in the literature. Tissue specialization is measured by average gene specificity. We introduce the formulae using a simple example and show their application in two datasets of gene expression in human tissues. Visualization of the positions of transcriptomes in a system of diversity and specialization coordinates makes it possible to understand at a glance their interrelations, summarizing in a powerful way which transcriptomes are richer in diversity of expressed genes, or which are relatively more specialized. The framework presented enlightens the relation among transcriptomes, allowing a better understanding of their changes through the development of the organism or in response to environmental stimuli.
