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
    def test_left_remove_ok(self):
        """Add left descriptor and make sure it can be removed just fine"""
        self._descriptor_add_ok("left")
        self._descriptor_remove_ok("left")
    
    @groups(UNIT_TESTS_GROUP)
    def test_left_remove_no_left(self):
        """Do not add left descriptor and make sure the removal is not fine"""
        self._descriptor_remove_not_ok("left")
        
    @groups(UNIT_TESTS_GROUP)
    def test_right_add_ok(self):
        """Add right descriptor and make sure all went fine"""
        self._descriptor_add_ok("right")
        
    @groups(UNIT_TESTS_GROUP)
    def test_center_add_ok(self):
        """Add center descriptor and make sure all went fine"""
        self._descriptor_add_ok("center")
        
    @groups(UNIT_TESTS_GROUP)
    def test_left_remove_wont_affect_others(self):
        """Add left descriptor and make sure it can be removed just fine, without affecting any other records"""
        self._descriptor_add_ok("right")
        self.assertEqual([{"id" : 1, "description" : "right", "data" : "abcd"}], 
                          ID.list())
        self._descriptor_add_ok("left")
        self.assertEqual([{"id" : 1, "description" : "right", "data" : "abcd"}, 
                          {"id" : 1, "description" : "left", "data" : "abcd"}], 
                          ID.list())
        self._descriptor_remove_ok("left")
        self.assertEqual([{"id" : 1, "description" : "right", "data" : "abcd"}], 
                          ID.list())
    
    @groups(UNIT_TESTS_GROUP)
    def test_left_removal_wont_affect_other_ids(self):
        """Add left descriptor to ID 1 and ID 2 and make sure ID 2 can be removed without affecting any other records"""
        self.assertEqual(True, ID.add(1, "left", "abcd"))
        self.assertEqual([{"id" : 1, "description" : "left", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(True, ID.add(2, "left", "abcd"))
        self.assertEqual([{"id" : 1, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "left", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(True, ID.remove(2, "left"))
        self.assertEqual([{"id" : 1, "description" : "left", "data" : "abcd"}], 
                          ID.list())
    
    @groups(UNIT_TESTS_GROUP)
    def test_left_add_not_ok(self):
        """Add left descriptor twice and make sure the second one doesn't work"""
        self._descriptor_add_ok("left")
        self._descriptor_add_not_ok("left")
    
    @groups(UNIT_TESTS_GROUP)
    def test_left_add_after_removal(self):
        """Add left descriptor, delete it and make sure it can be added again just fine"""
        self._descriptor_add_ok("left")
        self._descriptor_remove_ok("left")
        self._descriptor_add_ok("left")
    
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
    
    @groups(UNIT_TESTS_GROUP)
    def test_removal_all(self):
        """Add left and right descriptor to ID 1 and make sure it can be removed"""
        self.assertEqual(True, ID.add(1, "left", "abcd"))
        self.assertEqual(True, ID.add(1, "right", "abcd"))
        self.assertEqual(True, ID.remove_all(1, ["left","right"]))
        
    @groups(UNIT_TESTS_GROUP)
    def test_removal_all_without_single_descriptor(self):
        """Add left descriptor only to ID 1 and make sure remove all fails but didn't affected anything on the database"""
        self.assertEqual(True, ID.add(1, "left", "abcd"))
        self.assertEqual([{"id" : 1, "description" : "left", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(False, ID.remove_all(1, ["left","right"]))
        self.assertEqual([{"id" : 1, "description" : "left", "data" : "abcd"}], 
                          ID.list())
                          
    @groups(UNIT_TESTS_GROUP)
    def test_removal_all_without_all_descriptor(self):
        """Try to remove all from an ID that doesn't have anything and ensure it fails but leaves the database intact"""
        self.assertEqual(True, ID.add(2, "left", "abcd"))
        self.assertEqual(True, ID.add(2, "right", "abcd"))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(False, ID.remove_all(1, ["left","right"]))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
    
    @groups(UNIT_TESTS_GROUP)
    def test_removal_all_without_any_descriptor(self):
        """Try to remove all without any descriptor on the parameters list and ensure it ends ok but leaves the database intact"""
        self.assertEqual(True, ID.add(2, "left", "abcd"))
        self.assertEqual(True, ID.add(2, "right", "abcd"))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(True, ID.remove_all(2, []))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
                          
    @groups(UNIT_TESTS_GROUP)
    def test_removal_all_allow_adding_more(self):
        """Remove all from an ID and make sure we can add them again"""
        self.assertEqual(True, ID.add(2, "left", "abcd"))
        self.assertEqual(True, ID.add(2, "right", "abcd"))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
        self.assertEqual(True, ID.remove_all(2, ["left", "right"]))
        self.assertEqual(True, ID.add(2, "left", "abcd"))
        self.assertEqual(True, ID.add(2, "right", "abcd"))
        self.assertEqual([{"id" : 2, "description" : "left", "data" : "abcd"},
                          {"id" : 2, "description" : "right", "data" : "abcd"}], 
                          ID.list())
    
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