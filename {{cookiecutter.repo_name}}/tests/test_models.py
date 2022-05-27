#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.repo_name }}
------------

Tests for `{{ cookiecutter.repo_name }}` models module.
"""

from django.test import TestCase # type: ignore

from {{ cookiecutter.app_name }} import models # type: ignore 


class Test{{ cookiecutter.app_name|capitalize }}(TestCase): # type: ignore

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass
