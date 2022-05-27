# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" %} # type: ignore
from django.db.models import Model, CharField, DateTimeField, JSONField # type: ignore

{% for model in cookiecutter.models.split(',') %} #type: ignore
class {{ model.strip() }}(Model): #type: ignore
    pass

{% endfor %} #type: ignore
{% endif %} #type: ignore

class Transaction(Model): 
    id = CharField(max_length=100, primary_key=True) #type: ignore
    date_time = DateTimeField(auto_now=True) #type: ignore
    query = JSONField(default=dict)
    status = CharField(max_length=100, default="", null=True) #type: ignore
    versions = JSONField(default=dict)
    chp_app = CharField(max_length=128, null=True) #type: ignore
