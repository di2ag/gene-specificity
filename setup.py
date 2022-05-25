<<<<<<< HEAD
from setuptools import find_packages
from setuptools import setup

# get the app name
with open("./app_meta_data/setup/app_name.txt", "r") as f:
    app_name = f.read()
# make sure app_name was provided
if app_name == "":
    raise Exception("app_name not found in ./app_meta_data/setup/app_name.txt")

# get the author name(s)
with open("./app_meta_data/setup/author_name.txt", "r") as f:
    author_name = f.read()
# make sure author_name was provided
if author_name == "":
    raise Exception("author_name not found in ./app_meta_data/setup/author_name.txt")

# get description
with open("./app_meta_data/setup/description.txt", "r") as f:
    description = f.read()
# make sure description was provided
if description == "":
    raise Exception("description not found in ./app_meta_data/setup/description.txt")

# get long description
with open("./app_meta_data/setup/long_description.txt", "r") as f:
    long_description = f.read()
# make sure long_description was provided
if long_description == "":
    raise Exception("long_description not found in ./app_meta_data/setup/long_description.txt")

setup(
    name=app_name,
    version='1.0.0',
    description=description,
    author=author_name,
    author_email=author_email,
    packages=find_packages(),
    data_files=[
        (
            "./app_meta_data/setup/conflation_map/conflation_map.json",
            "./app_meta_data/setup/curies_database/curies_database.json",
            "./app_meta_data/setup/meta_knowledge_graph/meta_knowledge_graph.json",
        )
    ]
)
=======
from setuptools import setup

setup()
>>>>>>> f4fe133d92891d2594b70ae1fc36aa72185bf6c8
