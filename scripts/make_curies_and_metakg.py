import json
import csv
import os
from trapi_model.biolink.constants import *
from trapi_model.meta_knowledge_graph import MetaKnowledgeGraph

CURIE_PATH = '/home/public/data/ncats/curie_dir/'
TISSUES = 'tissue_mapping.json'
GENES = 'gene_curie_map.csv'

# get tissues mapping and gene mapping
tissues = json.load(open(os.path.join(CURIE_PATH,TISSUES)))
curie_to_gene = dict()
with open(os.path.join(CURIE_PATH,GENES)) as gene_file:
    reader = csv.reader(gene_file, delimiter=',')
    next(reader)
    for row in reader:
        curie_to_gene[row[1]] = row[0]

# load in gene specificity file. Keys represent the genes we consider in this app.
with open('/home/public/data/ncats/tissue_specificity/updated_curies/specificity_mean_genePK.json') as f:
    spec_data = json.load(f)
    app_specific_genes = list(spec_data.keys())

# build curie dict
curies = {BIOLINK_GROSS_ANATOMICAL_STRUCTURE_ENTITY.get_curie():dict(),
           BIOLINK_GENE_ENTITY.get_curie():dict()}

# add curie->tissue mapping
for key,val in tissues.items():
    curies[BIOLINK_GROSS_ANATOMICAL_STRUCTURE_ENTITY.get_curie()][val] = [key]

# add curie->gene mapping
for gene in app_specific_genes:
    if gene in curie_to_gene:
        curies[BIOLINK_GENE_ENTITY.get_curie()][gene] = [curie_to_gene[gene]]
    else:
        curies[BIOLINK_GENE_ENTITY.get_curie()][gene] = [None]

# make meta KG
metakg = MetaKnowledgeGraph('1.2', None)

## Add Nodes.
# Add preferred gene prefixes
genes = ['ENSEMBL','NCBIGene','HGNC']
metakg.add_node(BIOLINK_GENE_ENTITY, genes)

## Add Tissues
# Add preferred gene prefixes
tissues = ['UBERON','EFO']
metakg.add_node(BIOLINK_GROSS_ANATOMICAL_STRUCTURE_ENTITY, tissues)

## Add Edges.
# add gene->tissue
metakg.add_edge(
            BIOLINK_GENE_ENTITY,
            BIOLINK_GROSS_ANATOMICAL_STRUCTURE_ENTITY,
            BIOLINK_EXPRESSED_IN_ENTITY)

# expand with inverses
metakg = metakg.expand_with_inverses()

# save meta kg
metakg.json('meta_knowledge_graph.json')

# save curies
with open('curies.json', 'w') as f:
    json.dump(curies, f, indent=4)








