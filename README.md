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
              "ENSEMBL:ENSG00000132155"
            ],
            "categories": [
              "biolink:Gene"
            ]
          },
          "n1": {
            "categories": [
              "biolink:GrossAnatomicalStructure"
            ]
          }
        },
        "edges": {
          "e0": {
            "subject": "n0",
            "object": "n1",
            "predicates": [
              "biolink:expressed_in"
            ]
          }
        }
      }
    },
    "knowledge_graph": {},
    "results": {}
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
            "ENSEMBL:ENSG00000132155"
          ],
          "categories": [
            "biolink:Gene"
          ],
          "constraints": []
        },
        "n1": {
          "ids": null,
          "categories": [
            "biolink:GrossAnatomicalStructure"
          ],
          "constraints": []
        }
      },
      "edges": {
        "e0": {
          "predicates": [
            "biolink:expressed_in"
          ],
          "subject": "n0",
          "object": "n1",
          "constraints": []
        }
      }
    },
    "knowledge_graph": {
      "nodes": {
        "ENSEMBL:ENSG00000132155": {
          "name": "RAF1",
          "categories": [
            "biolink:Gene"
          ],
          "attributes": []
        },
        "UBERON:0014892": {
          "categories": [
            "biolink:GrossAnatomicalStructure"
          ],
          "attributes": []
        }
      },
      "edges": {
        "e0": {
          "predicate": "biolink:expressed_in",
          "subject": "ENSEMBL:ENSG00000132155",
          "object": "UBERON:0014892",
          "attributes": [
            {
              "attribute_type_id": "Specificity",
              "original_attribute_name": null,
              "value": 0.005393877080020849,
              "value_type_id": "biolink:has_evidence",
              "attribute_source": null,
              "value_url": null,
              "description": "Specificity value between a tissue and gene indicates a gene's RNA Sequence expression specificity to that tissue. Values closer to 0 indicate no expression specificity and values closer to 5.755 or log_2(54) (54 being the number of tissues used in this analysis) indicate complete specificity."
            },
            {
              "attribute_type_id": "primary_knowledge_source",
              "original_attribute_name": null,
              "value": "infores:connections-hypothesis",
              "value_type_id": "biolink:InformationResource",
              "attribute_source": "infores:connections-hypothesis",
              "value_url": "http://chp.thayer.dartmouth.edu",
              "description": "The Connections Hypothesis Provider from NCATS Translator."
            },
            {
              "attribute_type_id": "biolink:supporting_data_source",
              "original_attribute_name": null,
              "value": "infores:tcga",
              "value_type_id": "biolink:InformationResource",
              "attribute_source": "infores:gdc",
              "value_url": "https://gtexportal.org/home/",
              "description": "The Cancer Genome Atlas provided by the GDC Data Portal."
            }
          ]
        }
    },
    "results": [
      {
        "edge_bindings": {
          "e0": [
            {
              "id": "e0"
            }
          ]
        },
        "node_bindings": {
          "n0": [
            {
              "id": "ENSEMBL:ENSG00000132155"
            }
          ],
          "n1": [
            {
              "id": "UBERON:0014892"
            }
          ]
        }
      }
    ]
  },
  "logs": [],
  "workflow": []
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
  "nodes": {
    "biolink:Gene": {
      "id_prefixes": [
        "ENSEMBL",
        "NCBIGene",
        "HGNC"
      ]
    },
    "biolink:GrossAnatomicalStructure": {
      "id_prefixes": [
        "UBERON",
        "EFO"
      ]
    }
  },
  "edges": [
    {
      "subject": "biolink:Gene",
      "object": "biolink:GrossAnatomicalStructure",
      "predicate": "biolink:expressed_in"
    },
    {
      "subject": "biolink:GrossAnatomicalStructure",
      "object": "biolink:Gene",
      "predicate": "biolink:expresses"
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
