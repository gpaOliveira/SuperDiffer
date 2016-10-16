from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
from sqlalchemy import exc
import json

class DiffTestCases(SupperDifferBaseTestCase):

    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_any_descriptors(self):
        #Given some value is saved
        ID.add(1, "a", "b")

        #When the diff is requested without any descriptors to compare
        response = ID.diff(1, [])
        
        #Then None is returned
        self.assertEqual(None, response)
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_with_a_single_descriptors(self):
        #Given some value is saved
        ID.add(1, "a", "b")

        #When the diff is requested with a single descriptors to compare
        response = ID.diff(1, ["a"])
        
        #Then None is returned, as there are no pairs to compare
        self.assertEqual(None, response)
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_all_descriptors(self):
        #Given some value is saved
        ID.add(1, "a", "b")

        #When the diff between two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then None is returned, as not all the descriptors are found
        self.assertEqual(None, response)
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_id(self):
        #Given some values are saved
        ID.add(1, "a", "b")
        ID.add(1, "b", "b")

        #When the diff between two descriptors is requested with a different ID
        response = ID.diff(2, ["a","b"])
        
        #Then None is returned
        self.assertEqual(None, response)
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_not_equal_response(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "b")
        ID.add(1, "b", "ba")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"not equal", "diffs":[]}, response["a_b"])
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_1_char(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "b")
        ID.add(1, "b", "a")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[{"diff_start" : 0, "chain" : 1}]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_2_chars(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "ba")
        ID.add(1, "b", "ab")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[{"diff_start" : 0, "chain" : 2}]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_3_chars_middle_diff(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "b1b")
        ID.add(1, "b", "bbb")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[{"diff_start" : 1, "chain" : 1}]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_2_sequences_begin_middle(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "bab1b")
        ID.add(1, "b", "aacbb")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[
                                            {"diff_start" : 0, "chain" : 1},
                                            {"diff_start" : 2, "chain" : 2},
                                            ]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_2_sequences_middle_end(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "bab1b45")
        ID.add(1, "b", "bacbb49")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[
                                            {"diff_start" : 2, "chain" : 2},
                                            {"diff_start" : 6, "chain" : 1}
                                            ]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_3_sequences_begin_middle_end(self):
        #Given some values are saved with different lenght of values
        ID.add(1, "a", "bab1b45")
        ID.add(1, "b", "aacbb49")

        #When the diff between those two descriptors is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[
                                            {"diff_start" : 0, "chain" : 1},
                                            {"diff_start" : 2, "chain" : 2},
                                            {"diff_start" : 6, "chain" : 1}
                                            ]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_sequences_on_many_ids_request_1(self):
        #Given some values are saved with different lenght of values on different IDs
        ID.add(1, "a", "bab1b45")
        ID.add(1, "b", "aacbb49")
        ID.add(2, "a", "aabbb4512")
        ID.add(2, "b", "aacbb4513")

        #When the diff between two descriptors on ID 1 is requested
        response = ID.diff(1, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[
                                            {"diff_start" : 0, "chain" : 1},
                                            {"diff_start" : 2, "chain" : 2},
                                            {"diff_start" : 6, "chain" : 1}
                                            ]}, 
                        response["a_b"])
                        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_sequences_on_many_ids_request_2(self):
        #Given some values are saved with different lenght of values on different IDs
        ID.add(1, "a", "bab1b45")
        ID.add(1, "b", "aacbb49")
        ID.add(2, "a", "aabbb4512")
        ID.add(2, "b", "aacbb4513")

        #When the diff between two descriptors on ID 2 is requested
        response = ID.diff(2, ["a","b"])
        
        #Then a not equal response is returned, as the lenght of the values is different
        self.assertTrue("a_b" in response)
        self.assertEqual({"size":"equal", "diffs":[
                                            {"diff_start" : 2, "chain" : 1},
                                            {"diff_start" : 8, "chain" : 1}
                                            ]}, 
                        response["a_b"])
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_only_left_value_present(self):
        #Given Left description of ID = 1 is added but not the right one
        self.assertEqual(True, ID.add(1, "left", "abcd"))
        self.assertEqual(1, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 400 Bad Request is retrieved
        self.assertEqual("400 BAD REQUEST", result.status)
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_only_right_value_present(self):
        #Given right descriptors of ID = 1 is added but not the left one
        self.assertEqual(True, ID.add(1, "right", "abcd"))
        self.assertEqual(1, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 400 Bad Request is retrieved
        self.assertEqual("400 BAD REQUEST", result.status)
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_left_right_different_lenghts(self):
        #Given left and right descriptors of ID = 1 are added, but with different value lenghts
        self.assertEqual(True, ID.add(1, "left", "abcde"))
        self.assertEqual(True, ID.add(1, "right", "abcd"))
        self.assertEqual(2, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 200 is retrieved
        self.assertEqual("200 OK", result.status)
        
        #And the response json states that the size is different
        self.assertEqual({"size":"not equal", "diffs":[]}, json.loads(result.data))
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())
    
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_left_right_equal_lenghts_values(self):
        #Given left and right descriptors of ID = 1 are added, with equal values
        self.assertEqual(True, ID.add(1, "left", "abcde"))
        self.assertEqual(True, ID.add(1, "right", "abcde"))
        self.assertEqual(2, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 200 is retrieved
        self.assertEqual("200 OK", result.status)
        
        #And the response json states that the size is different
        self.assertEqual({"size":"equal", "diffs":[]}, json.loads(result.data))
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_left_right_1_diff_on_values(self):
        #Given left and right descriptors of ID = 1 are added, with different values
        self.assertEqual(True, ID.add(1, "left", "abc1de"))
        self.assertEqual(True, ID.add(1, "right", "abc2de"))
        self.assertEqual(2, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 200 is retrieved
        self.assertEqual("200 OK", result.status)
        
        #And the response json states that the size is different
        self.assertEqual({"size":"equal", "diffs":[{"diff_start" : 3, "chain" : 1}]}, json.loads(result.data))
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_left_right_1_diff_on_other_values(self):
        #Given left and right descriptors of ID = 1 are added, with different values
        self.assertEqual(True, ID.add(1, "left", "abc1de"))
        self.assertEqual(True, ID.add(1, "right", "abc2de"))
        self.assertEqual(True, ID.add(2, "left", "abc1de124"))
        self.assertEqual(True, ID.add(2, "right", "abc1de123"))
        self.assertEqual(4, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 2
        result = self.app.get("/v1/diff/2")
        
        #Then a 200 is retrieved
        self.assertEqual("200 OK", result.status)
        
        #And the response json states that the size is different
        self.assertEqual({"size":"equal", "diffs":[{"diff_start" : 8, "chain" : 1}]}, json.loads(result.data))
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())