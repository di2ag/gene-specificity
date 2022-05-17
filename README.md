# Enter APP Name Here
ENTER APP DESCRIPTION HERE

## Trapi Transaction
------------------------------------------------------------------------

Example of the Trapi Query, Response, and Meta Knowledge Graph Objects
### Query
<!-- create a query example for every supported query type in the meta knowledge graph for this app -->
```jsonc
// query object
// reference: https://github.com/NCATSTranslator/ReasonerAPI#message
{
  // message object
  // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#message-
  "message": {
    // query graph object
    // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#querygraph-
    "query_graph": {
      // nodes field
      // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#fixed-fields-9
      "nodes": {
        // subject node
        // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#qnode-
        "n0": {
          // biolink curie identifier
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#curie-
          "ids": [],
          // biolink category types
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#biolinkentity-
          "categories": [],
          // indicates that this QNode MAY have multiple KnowledgeGraph Nodes bound to it within each Result
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#fixed-fields-10
          "is_set": false,
          // A list of contraints applied to a query node
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#queryconstraint-
          "constraints"[]
        },
        // object node
        // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#qnode-
        "n0": {
          // biolink curie identifier
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#curie-
          "ids": [],
          // biolink category types
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#biolinkentity-
          "categories": [],
          // indicates that this QNode MAY have multiple KnowledgeGraph Nodes bound to it within each Result
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#fixed-fields-10
          "is_set": false,
          // A list of contraints applied to a query node
          // reference: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#queryconstraint-
          "constraints"[]
        }
      },
      "edges": {
        "e0": {
          // biolink predicate types
          "predicates": [
            // <enter predicate types>
          ],
          "subject": "n0",
          "object": "n1",
          "constraints": [
            // enter edge constraints here
          ]
        }
      }
    }
  }
}
```

### Response
```json
{
  
}
```

### Meta Knowledge Graph
```json
{
  
}
```

## References
#### Example Reference 1
  Link: [example reference home page](www.example.com)
  Description: <enter description for reference 1 here\>
### Example Reference 2
