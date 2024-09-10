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
          "set_interpretation": "BATCH",
          "constraints": []
        },
        "n2": {
          "ids": null,
          "categories": [
            "biolink:Protein",
            "biolink:Gene"
          ],
          "set_interpretation": "BATCH",
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
          "attributes": [],
          "is_set": null
        },
        "UBERON:0008952": {
          "categories": [
            "biolink:GrossAnatomicalStructure"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000122852": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000185303": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000168484": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000168878": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000225615": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000166961": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000283298": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000149021": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000164265": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000230657": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000259094": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000273877": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000281652": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000203878": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000131400": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000260695": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000225876": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000133661": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        },
        "ENSEMBL:ENSG00000277569": {
          "categories": [
            "biolink:Gene"
          ],
          "name": null,
          "attributes": [],
          "is_set": null
        }
      },
      "edges": {
        "be6262e0fb1b": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 1.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 5.734026963422729,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "6eceafaac887": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 5.558965492623509,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.9694697161495865,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "26d7737d2a52": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 5.429707244074908,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.9469274000124046,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "b2beb1618395": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 5.373584961634749,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.9371398139410166,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "b465fd6d6f0a": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 5.159419899199448,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8997899612456148,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "9eae3875d103": {
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
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8535995031315986,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.894562566920831,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "affb2bb98523": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8460917057665672,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.851512654393827,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "e1a9e88ab793": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.813351699194642,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8394365303649493,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "c69732b4e27d": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8372035895385825,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.800547956288527,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "9aac703a95b0": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.730605547974056,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.8250058079863448,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "ef659a3bec31": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.7668258437131956,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 4.3970000641008475,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "a2a93f10ec7d": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.741740204899714,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.6525501586874666,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "9fb3a8c064a2": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.6223588014190778,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.5686221482604443,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "5681ef08ae49": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.4737342230950787,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.6058105839498099,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "2f1f4f9e0090": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.5900644436191647,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.3834454298693206,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "5883f1f4a5f3": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.3002325393020224,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.5755523230626844,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "cd74aa7117b1": {
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
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.5527032123735791,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.1692151225204617,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "56dab35384d5": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 3.019149891359312,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.5265322103677613,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "337ccb4cf18a": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 2.7056658235593245,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.47186137086880225,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            }
          ]
        },
        "40704c2fa2da": {
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
              "attribute_type_id": "Specificity P-value",
              "value": 0.0,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "P-val assessing significance of unnormalized Specificity value.",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Unnormalized)",
              "value": 2.683053565999062,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are unnormalized between range [0, 5.5].",
              "attributes": null
            },
            {
              "attribute_type_id": "Specificity (Normalized)",
              "value": 0.4679178495521943,
              "value_type_id": "biolink:has_evidence",
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": "Specificity values for gene-tissue edges measure the specificity of a gene's transcription across all tissues included in https://www.gtexportal.org/home/samplingSitePage. Values are normalized between range [0,1].",
              "attributes": null
            },
            {
              "attribute_type_id": "agent_type",
              "value": "computational_model",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
              "attributes": null
            },
            {
              "attribute_type_id": "knowledge_level",
              "value": "statistical_association",
              "value_type_id": null,
              "original_attribute_name": null,
              "value_url": null,
              "attribute_source": null,
              "description": null,
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
              "id": "ENSEMBL:ENSG00000249387",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "be6262e0fb1b",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000122852",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "6eceafaac887",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000185303",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "26d7737d2a52",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000168484",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "b2beb1618395",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000168878",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "b465fd6d6f0a",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000225615",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "9eae3875d103",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000166961",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "affb2bb98523",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000283298",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "e1a9e88ab793",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000149021",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "c69732b4e27d",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000164265",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "9aac703a95b0",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000230657",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "ef659a3bec31",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000259094",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "a2a93f10ec7d",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000273877",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "9fb3a8c064a2",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000281652",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "5681ef08ae49",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000203878",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "2f1f4f9e0090",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000131400",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "5883f1f4a5f3",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000260695",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "cd74aa7117b1",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000225876",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "56dab35384d5",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000133661",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "337ccb4cf18a",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      },
      {
        "node_bindings": {
          "n2": [
            {
              "id": "ENSEMBL:ENSG00000277569",
              "query_id": null,
              "attributes": []
            }
          ],
          "n1": [
            {
              "id": "UBERON:0008952",
              "query_id": "UBERON:0002048",
              "attributes": []
            }
          ]
        },
        "analyses": [
          {
            "resource_id": "infores:connections-hypothesis",
            "edge_bindings": {
              "e1": [
                {
                  "id": "40704c2fa2da",
                  "attributes": []
                }
              ]
            },
            "score": null,
            "support_graphs": null,
            "scoring_method": null,
            "attributes": []
          }
        ]
      }
    ],
    "auxiliary_graphs": null
  },
  "logs": [
    {
      "timestamp": "2024-09-10T15:07:41.668683",
      "level": "INFO",
      "message": "Running message.",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.668699",
      "level": "INFO",
      "message": "Getting message templates.",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.668861",
      "level": "INFO",
      "message": "Checking template matches for gene_specificity",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.673699",
      "level": "INFO",
      "message": "Detected 1 matches for gene_specificity",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.673709",
      "level": "INFO",
      "message": "Constructing queries on matching templates",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.674350",
      "level": "INFO",
      "message": "Sending 1 consistent queries",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.684542",
      "level": "INFO",
      "message": "Wildcard detected",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.686539",
      "level": "INFO",
      "message": "Found results for UBERON:0008952",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.705861",
      "level": "INFO",
      "message": "Received responses from gene_specificity",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.758129",
      "level": "INFO",
      "message": "Checking template matches for gennifer",
      "code": null
    },
    {
      "timestamp": "2024-09-10T15:07:41.762313",
      "level": "INFO",
      "message": "Detected 0 matches for gennifer",
      "code": null
    }
  ],
  "trapi_version": "1.5",
  "biolink_version": "4.2.0",
  "status": "Success",
  "id": "1b8cd76a-9b64-49f1-834f-c010828a2dbf",
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
