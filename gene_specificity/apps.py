# -*- coding: utf-8
from django.apps import AppConfig


class GeneSpecificityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ cookiecutter.app_name }}'
    label = '{{ cookiecutter.app_name }}'
