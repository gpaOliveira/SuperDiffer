from SuperDiffer.tests import *
from SuperDiffer.tests.test_base_descriptor import *
from SuperDiffer.id import controllers as ID
import json

class AddDescriptorTestCase(SupperDifferBaseDescriptorTestCase):
    """Test cases to verify and document the Add behavior on the controller and on the endpoints"""

    @groups(UNIT_TESTS_GROUP)
    def test_left_add_ok(self):
        """Add left descriptor and make sure all went fine"""
        self._descriptor_add_ok("left")
        
    @groups(UNIT_TESTS_GROUP)
    def test_right_add_ok(self):
        """Add right descriptor and make sure all went fine"""
        self._descriptor_add_ok("right")
        
    @groups(UNIT_TESTS_GROUP)
    def test_center_add_ok(self):
        """Add center descriptor and make sure all went fine"""
        self._descriptor_add_ok("center")
        
    @groups(UNIT_TESTS_GROUP)
    def test_left_add_not_ok(self):
        """Add left descriptor twice and make sure the second one doesn't work"""
        self._descriptor_add_ok("left")
        self._descriptor_add_not_ok("left")
        
    @groups(UNIT_TESTS_GROUP)
    def test_right_add_not_ok(self):
        """Add right descriptor twice and make sure the second one doesn't work"""
        self._descriptor_add_ok("right")
        self._descriptor_add_not_ok("right")
        
    @groups(UNIT_TESTS_GROUP)
    def test_center_add_not_ok(self):
        """Add center descriptor twice and make sure the second one doesn't work"""
        self._descriptor_add_ok("center")
        self._descriptor_add_not_ok("center")
        
    @groups(UNIT_TESTS_GROUP)
    def test_mixed_add(self):
        """Mix add descriptors to make sure the twice add of each doesn't work"""
        self._descriptor_add_ok("center")
        self._descriptor_add_ok("left")
        self._descriptor_add_ok("right")
        self._descriptor_add_not_ok("center")
        self._descriptor_add_not_ok("left")
        self._descriptor_add_not_ok("right")
    
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_201(self):
        """Post to left endpoint and make sure all went well"""
        self._integration_descriptor_add_201("left")
    
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_right_201(self):
        """Post to right endpoint and make sure all went well"""
        self._integration_descriptor_add_201("right")
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_repeated_left_value(self):
        """Post to left endpoint twice and make sure the second one doesn't work (right endpoint works the same so we don't need to cover it with another test)"""
        self._integration_descriptor_add_201("left", {"data":"abcd"})
        self._integration_descriptor_add_400("left", {"data":"abcf"})
                         
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_left_400_due_to_bad_base64(self):
        """Post to left endpoint with bad base64 data and make sure it doesn't work"""
        self._integration_descriptor_add_400("left", {"data":"abc"})
        self._integration_descriptor_add_400("left", {"data":[]})
        self._integration_descriptor_add_400("left", {"nodata":"abcd"})
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_center_404_no_endpoint(self):
        """Post to center endpoint to make sure it doesn't exists"""
        self._integration_descriptor_add_404("center", {"data":"abcd"})
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_mixed(self):
        """Mix posting to left and right endpoints twice and make sure the second one of each doesn't work"""
        self._integration_descriptor_add_201("left", {"data":"abcd"})
        self._integration_descriptor_add_201("right", {"data":"abcd"})
        self._integration_descriptor_add_400("left", {"data":"abcf"})
        self._integration_descriptor_add_400("right", {"data":"abcf"})
    
    @groups(INTEGRATON_TESTS_GROUP)    
    def test_integration_id_nan_404(self):
        """Post to right or left with a not-a-number ID to make sure it doesn't exists"""
        self._integration_id_as_nan_404()