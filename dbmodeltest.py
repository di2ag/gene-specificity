import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gene_specificity_testproj.gene_specificity_testproj.settings')

from django.db import connection

tables = connection.introspection.table_names()
seen_models = connection.introspection.installed_models(tables)