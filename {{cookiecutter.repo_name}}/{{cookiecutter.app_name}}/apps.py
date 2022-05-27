# -*- coding: utf-8
from django.apps import AppConfig # type: ignore


class {{ cookiecutter.app_config_name }}(AppConfig): # type: ignore
    name = '{{ cookiecutter.app_name }}'
