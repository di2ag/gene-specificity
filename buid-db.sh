#!/bin/bash

echo 'loading gene specifity data'
python3 /workspace/gene_specificity_testproj/manage.py loaddata -v3 /workspace/fixtures/SpecificityMeanGene.json
python3 /workspace/gene_specificity_testproj/manage.py loaddata -v3 /workspace/fixtures/SpecificityMeanTissue.json
python3 /workspace/gene_specificity_testproj/manage.py loaddata -v3 /workspace/fixtures/SpecificityMedianGene.json
python3 /workspace/gene_specificity_testproj/manage.py loaddata -v3 /workspace/fixtures/SpecificityMedianTissue.json

echo "Dumping data into Fixture."
python3 /workspace/gene_specificity_testproj/manage.py dumpdata -o /workspace/gene_specificity_testproj/chp_db_fixture.json.gz