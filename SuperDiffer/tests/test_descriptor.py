from SuperDiffer.tests import *
from SuperDiffer.tests.test_base_descriptor import *
from SuperDiffer.id import controllers as ID
import json

class AddDescriptortTestCase(SupperDifferBaseDescriptortTestCase):

    @groups(UNIT_TESTS_GROUP)
    def test_left_add_ok(self):
        self._descriptor_add_ok("left")
        
    @groups(UNIT_TESTS_GROUP)
    def test_right_add_ok(self):
        self._descriptor_add_ok("right")
        
    @groups(UNIT_TESTS_GROUP)
    def test_center_add_ok(self):
        self._descriptor_add_ok("center")
        
    @groups(UNIT_TESTS_GROUP)
    def test_left_add_not_ok(self):
        self._descriptor_add_ok("left")
        self._descriptor_add_not_ok("left")
        
    @groups(UNIT_TESTS_GROUP)
    def test_right_add_not_ok(self):
        self._descriptor_add_ok("right")
        self._descriptor_add_not_ok("right")
        
    @groups(UNIT_TESTS_GROUP)
    def test_center_add_not_ok(self):
        self._descriptor_add_ok("center")
        self._descriptor_add_not_ok("center")
        
    @groups(UNIT_TESTS_GROUP)
    def test_mixed_add(self):
        self._descriptor_add_ok("center")
        self._descriptor_add_ok("left")
        self._descriptor_add_ok("right")
        self._descriptor_add_not_ok("center")
        self._descriptor_add_not_ok("left")
        self._descriptor_add_not_ok("right")
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_201(self):
        self._integration_descriptor_add_201("left", json.dumps({ "data" : "a"}))
    
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_right_201(self):
        self._integration_descriptor_add_201("right", json.dumps({ "data" : "a"}))
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_repeated_left_value(self):
        self._integration_descriptor_add_201("left", json.dumps({ "data" : "a"}))
        self._integration_descriptor_add_400("left", json.dumps({ "data" : "b"}))
                         
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_bad_json(self):
        self._integration_descriptor_add_201("left", json.dumps({ "data" : "a"}))
        self._integration_descriptor_add_400("left", "[\"a\":1]")
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_center_404_no_endpoint(self):
        self._integration_descriptor_add_404("center", json.dumps({ "data" : "a"}))
        self._integration_descriptor_add_404("center", "[\"a\":1]")
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_mixed(self):
        self._integration_descriptor_add_201("left", json.dumps({ "data" : "a"}))
        self._integration_descriptor_add_201("right", json.dumps({ "data" : "a"}))
        self._integration_descriptor_add_400("left", json.dumps({ "data" : "b"}))
        self._integration_descriptor_add_400("right", json.dumps({ "data" : "b"}))