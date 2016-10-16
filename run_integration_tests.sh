#!/usr/bin/env bash
#Taken from https://github.com/valermor/nose2-tests-recipes/
nose2 --plugin nose2.plugins.attrib -A group='INTEGRATION_TESTS_GROUP' --with-coverage --coverage SuperDiffer
