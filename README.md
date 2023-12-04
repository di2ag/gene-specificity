# Gene Specificity Index
The Gene Specificity Index exposes a rank ordering over gene-tissue RNA Sequence relationships. Genes that have a high expression and express only in a small subset of tissues will be ranked higher than genes that have a lower expression and express in many tissue types. We build the Gene Specificity Index using data from the [Genotype-Tissue Expression (GTEx) project](#gtex). GTEx exposes RNA Sequence data expression from samples over a large range of tissues (54). We use the gene expression values of these samples to build tissue specific profiles that can be used to compare. The methodology is taken from [Defining diversity, specialization, and gene specificity in transcriptomes through information theory](#defining-diversity-specialization-and-gene-specificity-in-transcriptomes-through-information-theory) by Octavio Martínez and M. Humberto Reyes-Valdés. Specificity values range from 0 to 5.755 (log<sub>2</sub>(x), where x is the number of tissues) where values closer to 0 indicate no specificity and values closer to 5.755 indicicate complete specificity

## Trapi Transaction
Examples of the Trapi Query, Response, and Meta Knowledge Graph Objects that this app supports.

### Meta Knowledge Graph
<!-- 
  Reference Meta Knowledge Graph for this app
  reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#query-
  -->
<details>
  <summary> Click to view json example</summary>

  ```json
  {
    "nodes": {
      "biolink:Gene": {
        "id_prefixes": [
          "ENSEMBL"
        ],
        "attributes": null
      },
      "biolink:GrossAnatomicalStructure": {
        "id_prefixes": [
          "UBERON",
          "EFO"
        ],
        "attributes": null
      }
    },
    "edges": [
      {
        "subject": "biolink:Gene",
        "predicate": "biolink:expressed_in",
        "object": "biolink:GrossAnatomicalStructure",
        "qualifiers": null,
        "attributes": null,
        "knowledge_types": null,
        "association": null
      },
      {
        "subject": "biolink:GrossAnatomicalStructure",
        "predicate": "biolink:expresses",
        "object": "biolink:Gene",
        "qualifiers": null,
        "attributes": null,
        "knowledge_types": null,
        "association": null
      }
    ]
  }
  ```
</details>

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
            "edges": {
                "e1": {
                    "object": "n1",
                    "predicates": [
                        "biolink:expressed_in"
                    ],
                    "subject": "n2"
                }
            },
            "nodes": {
                "n1": {
                    "categories": [
                        "biolink:GrossAnatomicalStructure"
                    ],
                    "ids": [
                        "UBERON:0002048"
                    ]
                },
                "n2": {
                    "categories": [
                        "biolink:Protein",
                        "biolink:Gene"
                    ]
                }
            }
        }
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
                "n1": {
                    "ids": [
                        "UBERON:0002048"
                    ],
                    "categories": [
                        "biolink:GrossAnatomicalStructure"
                    ],
                    "is_set": false,
                    "constraints": []
                },
                "n2": {
                    "ids": null,
                    "categories": [
                        "biolink:Protein",
                        "biolink:Gene"
                    ],
                    "is_set": false,
                    "constraints": []
                }
            },
            "edges": {
                "e1": {
                    "subject": "n2",
                    "object": "n1",
                    "knowledge_type": null,
                    "predicates": [
                        "biolink:expressed_in"
                    ],
                    "attribute_constraints": [],
                    "qualifier_constraints": []
                }
            }
        },
        "knowledge_graph": {
            "nodes": {
                "ENSEMBL:ENSG00000249387": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "UBERON:0008952": {
                    "categories": [
                        "biolink:GrossAnatomicalStructure"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000122852": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000185303": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000168484": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000168878": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000225615": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000166961": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000283298": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000149021": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000164265": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000230657": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000259094": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000273877": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000281652": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000203878": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000131400": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000260695": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000225876": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000133661": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000277569": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000267137": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000196260": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000261143": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000226594": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000149435": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000231698": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000047936": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000178084": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000108576": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                },
                "ENSEMBL:ENSG00000121075": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "name": null,
                    "attributes": null
                }
            },
            "edges": {
                "c8077c03627c": {
                    "subject": "ENSEMBL:ENSG00000249387",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 5.734026963422729,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "f344439c8671": {
                    "subject": "ENSEMBL:ENSG00000122852",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 5.558965492623509,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "45ffe67a459c": {
                    "subject": "ENSEMBL:ENSG00000185303",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 5.429707244074908,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "0c38e15cb68c": {
                    "subject": "ENSEMBL:ENSG00000168484",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 5.373584961634749,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "0990a4150c9e": {
                    "subject": "ENSEMBL:ENSG00000168878",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 5.159419899199448,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "2898a250ea49": {
                    "subject": "ENSEMBL:ENSG00000225615",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.894562566920831,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "a2b267cae3fb": {
                    "subject": "ENSEMBL:ENSG00000166961",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.851512654393827,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "97f9f4a7899a": {
                    "subject": "ENSEMBL:ENSG00000283298",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.813351699194642,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "cb2dfac81b72": {
                    "subject": "ENSEMBL:ENSG00000149021",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.800547956288527,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "eb02779b9aaa": {
                    "subject": "ENSEMBL:ENSG00000164265",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.730605547974056,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "23a0d946dfa1": {
                    "subject": "ENSEMBL:ENSG00000230657",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 4.3970000641008475,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "5aa16bba0e7b": {
                    "subject": "ENSEMBL:ENSG00000259094",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.741740204899714,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "e7972a3be071": {
                    "subject": "ENSEMBL:ENSG00000273877",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.5686221482604443,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "e0da47628336": {
                    "subject": "ENSEMBL:ENSG00000281652",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.4737342230950787,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "ad5eb6226aa5": {
                    "subject": "ENSEMBL:ENSG00000203878",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.3834454298693206,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "a8e3e613932a": {
                    "subject": "ENSEMBL:ENSG00000131400",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.3002325393020224,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "973fec2f488b": {
                    "subject": "ENSEMBL:ENSG00000260695",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.1692151225204617,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "f7ceff293296": {
                    "subject": "ENSEMBL:ENSG00000225876",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 3.019149891359312,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "0c2a65453027": {
                    "subject": "ENSEMBL:ENSG00000133661",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.7056658235593245,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "075850922e03": {
                    "subject": "ENSEMBL:ENSG00000277569",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.683053565999062,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "e67b19c372af": {
                    "subject": "ENSEMBL:ENSG00000267137",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.6462283663213797,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "c7382d2f543e": {
                    "subject": "ENSEMBL:ENSG00000196260",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.6420583237541613,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "f1daa49ab5ca": {
                    "subject": "ENSEMBL:ENSG00000261143",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.536014798517655,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "eb6e64ba60a6": {
                    "subject": "ENSEMBL:ENSG00000226594",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.484500940218985,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "833efc0238a7": {
                    "subject": "ENSEMBL:ENSG00000149435",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.4596014693683776,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "3abbb6d32f84": {
                    "subject": "ENSEMBL:ENSG00000231698",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.4193977860747857,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "9e8cfa630a08": {
                    "subject": "ENSEMBL:ENSG00000047936",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.4093159707169485,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "cb1f8bf42a51": {
                    "subject": "ENSEMBL:ENSG00000178084",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.38770634925665,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        }
                    ]
                },
                "77af992adc41": {
                    "subject": "ENSEMBL:ENSG00000108576",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.298649161228743,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                },
                "0ccf8ccafe6f": {
                    "subject": "ENSEMBL:ENSG00000121075",
                    "object": "UBERON:0008952",
                    "predicate": "biolink:expressed_in",
                    "sources": [
                        {
                            "resource_id": "infores:gtex",
                            "resource_role": "supporting_data_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        },
                        {
                            "resource_id": "infores:connections-hypothesis",
                            "resource_role": "primary_knowledge_source",
                            "upstream_resource_ids": null,
                            "source_record_urls": null
                        }
                    ],
                    "qualifiers": null,
                    "attributes": [
                        {
                            "attribute_type_id": "primary_knowledge_source",
                            "value": "infores:connections-hypothesis",
                            "value_type_id": null,
                            "original_attribute_name": null,
                            "value_url": "https://github.com/di2ag/gene-specificity",
                            "attribute_source": null,
                            "description": "The Connections Hypothesis Provider from NCATS Translator",
                            "attributes": null
                        },
                        {
                            "attribute_type_id": "Specificity",
                            "value": 2.285690830927124,
                            "value_type_id": "biolink:has_evidence",
                            "original_attribute_name": null,
                            "value_url": null,
                            "attribute_source": null,
                            "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity.",
                            "attributes": null
                        }
                    ]
                }
            }
        },
        "results": [
            {
                "node_bindings": {
                    "n2": [
                        {
                            "id": "ENSEMBL:ENSG00000164265",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000166961",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000260695",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000108576",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000259094",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000230657",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000133661",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000281652",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000196260",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000047936",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000261143",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000168484",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000225876",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000131400",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000168878",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000283298",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000226594",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000267137",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000203878",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000121075",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000231698",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000273877",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000225615",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000178084",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000149021",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000185303",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000277569",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000149435",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000249387",
                            "query_id": null,
                            "attributes": null
                        },
                        {
                            "id": "ENSEMBL:ENSG00000122852",
                            "query_id": null,
                            "attributes": null
                        }
                    ],
                    "n1": [
                        {
                            "id": "UBERON:0008952",
                            "query_id": "UBERON:0002048",
                            "attributes": null
                        }
                    ]
                },
                "analyses": [
                    {
                        "resource_id": "infores:connections-hypothesis",
                        "edge_bindings": {
                            "e1": [
                                {
                                    "id": "c8077c03627c",
                                    "attributes": null
                                },
                                {
                                    "id": "f1daa49ab5ca",
                                    "attributes": null
                                },
                                {
                                    "id": "97f9f4a7899a",
                                    "attributes": null
                                },
                                {
                                    "id": "0c2a65453027",
                                    "attributes": null
                                },
                                {
                                    "id": "a8e3e613932a",
                                    "attributes": null
                                },
                                {
                                    "id": "833efc0238a7",
                                    "attributes": null
                                },
                                {
                                    "id": "3abbb6d32f84",
                                    "attributes": null
                                },
                                {
                                    "id": "f344439c8671",
                                    "attributes": null
                                },
                                {
                                    "id": "e7972a3be071",
                                    "attributes": null
                                },
                                {
                                    "id": "77af992adc41",
                                    "attributes": null
                                },
                                {
                                    "id": "f7ceff293296",
                                    "attributes": null
                                },
                                {
                                    "id": "0ccf8ccafe6f",
                                    "attributes": null
                                },
                                {
                                    "id": "5aa16bba0e7b",
                                    "attributes": null
                                },
                                {
                                    "id": "2898a250ea49",
                                    "attributes": null
                                },
                                {
                                    "id": "9e8cfa630a08",
                                    "attributes": null
                                },
                                {
                                    "id": "0990a4150c9e",
                                    "attributes": null
                                },
                                {
                                    "id": "eb6e64ba60a6",
                                    "attributes": null
                                },
                                {
                                    "id": "0c38e15cb68c",
                                    "attributes": null
                                },
                                {
                                    "id": "cb2dfac81b72",
                                    "attributes": null
                                },
                                {
                                    "id": "a2b267cae3fb",
                                    "attributes": null
                                },
                                {
                                    "id": "eb02779b9aaa",
                                    "attributes": null
                                },
                                {
                                    "id": "973fec2f488b",
                                    "attributes": null
                                },
                                {
                                    "id": "23a0d946dfa1",
                                    "attributes": null
                                },
                                {
                                    "id": "e0da47628336",
                                    "attributes": null
                                },
                                {
                                    "id": "cb1f8bf42a51",
                                    "attributes": null
                                },
                                {
                                    "id": "c7382d2f543e",
                                    "attributes": null
                                },
                                {
                                    "id": "075850922e03",
                                    "attributes": null
                                },
                                {
                                    "id": "e67b19c372af",
                                    "attributes": null
                                },
                                {
                                    "id": "45ffe67a459c",
                                    "attributes": null
                                },
                                {
                                    "id": "ad5eb6226aa5",
                                    "attributes": null
                                }
                            ]
                        },
                        "score": null,
                        "support_graphs": null,
                        "scoring_method": null,
                        "attributes": null
                    }
                ]
            }
        ],
        "auxiliary_graphs": null
    },
    "logs": [
        {
            "timestamp": "2023-07-17T13:14:08.965023",
            "level": "INFO",
            "message": "Running message.",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.965038",
            "level": "INFO",
            "message": "Getting message templates.",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.965196",
            "level": "INFO",
            "message": "Checking template matches for gene_specificity",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.970389",
            "level": "INFO",
            "message": "Detected 1 matches for gene_specificity",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.970398",
            "level": "INFO",
            "message": "Constructing queries on matching templates",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.971413",
            "level": "INFO",
            "message": "Sending 1 consistent queries",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.978405",
            "level": "INFO",
            "message": "Wildcard detected",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.980608",
            "level": "INFO",
            "message": "Found results for UBERON:0008952",
            "code": null
        },
        {
            "timestamp": "2023-07-17T13:14:08.992424",
            "level": "INFO",
            "message": "Received responses from gene_specificity",
            "code": null
        }
    ],
    "trapi_version": "1.4",
    "biolink_version": "3.1.2",
    "status": "Success",
    "id": "2552ca69-48c0-4c6f-828e-4fc8d5b7f4fb",
    "workflow": [
        {
            "id": "lookup"
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
