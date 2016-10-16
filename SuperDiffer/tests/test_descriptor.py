from SuperDiffer.tests import *
from SuperDiffer.tests.test_base_descriptor import *
from SuperDiffer.id import controllers as ID
import json

class AddDescriptorTestCase(SupperDifferBaseDescriptorTestCase):

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
        self._integration_descriptor_add_201("left")
    
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_right_201(self):
        self._integration_descriptor_add_201("right")
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_repeated_left_value(self):
        self._integration_descriptor_add_201("left", {"data":"abcd"})
        self._integration_descriptor_add_400("left", {"data":"abcf"})
                         
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_bad_base64(self):
        self._integration_descriptor_add_400("left", {"data":"abc"})
        self._integration_descriptor_add_400("left", {"data":[]})
        self._integration_descriptor_add_400("left", {"nodata":"abcd"})
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_center_404_no_endpoint(self):
        self._integration_descriptor_add_404("center", {"data":"abcd"})
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_mixed(self):
        self._integration_descriptor_add_201("left", {"data":"abcd"})
        self._integration_descriptor_add_201("right", {"data":"abcd"})
        self._integration_descriptor_add_400("left", {"data":"abcf"})
        self._integration_descriptor_add_400("right", {"data":"abcf"})
    
    @groups(INTEGRATON_TESTS_GROUP)    
    def test_integration_id_nan_404(self):
        self._integration_id_as_nan_404()