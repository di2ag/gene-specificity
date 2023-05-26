from setuptools import find_packages, setup

__version__='1.0'

# read requirements from requirements.txt for setup.py
with open('requirements.txt') as f:
    REQUIRED_PACKAGES = f.read().splitlines()

setup(
    name='gene_specificity',
    version=__version__,
    author='Luke Veenhuis',
    author_email='luke.j.veenhuis@dartmouth.edu',
    description='gene specificity lookup app for Connections Hypothesis Provider',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    python_requires='>=3.8',
    data_files=[
        ('',
            [
                'gene_specificity/app_meta_data/meta_knowledge_graph.json',
                ]
            )
        ],
    package_data={'gene_specificity': ['app_meta_data/conflation_map.json', 'app_meta_data/curies.json', 'app_meta_data/epc.json', 'app_meta_data/meta_knowledge_graph.json']},
    dependency_links=[
    ]
)
