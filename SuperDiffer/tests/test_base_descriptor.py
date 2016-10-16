from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
import json
import pdb

class SupperDifferBaseDescriptorTestCase(SupperDifferBaseTestCase):

    def _descriptor_add_ok(self, descriptor, value = "abcd"):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #When a model entry is added
        model_entry_status = ID.add(1, descriptor, value)
        
        #Then the model entry status is ok
        self.assertEqual(True, model_entry_status)
        
        #And the initial db count was incremented by 1
        self.assertEqual(initial_db_count + 1, ID.count())
        
        #And the data from db list model has the entry as used in the end
        self.assertEqual({"id" : 1, "description" : descriptor, "data" : value}, ID.list()[-1])        
        
    def _descriptor_add_not_ok(self, descriptor, value = "abcd"):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.list()
        
        #When a model entry is added
        model_entry_status = ID.add(1, descriptor, value)
        
        #Then the model entry status is not ok
        self.assertEqual(False, model_entry_status)
        
        #Then the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.list())
        
        #And the initial db count is the same as the beggining
        self.assertEqual(initial_db_count, ID.count())

    def _integration_descriptor_add_201(self, descriptor, data_to_send = {"data":"abcd"}):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = json.dumps(data_to_send),
                               content_type = "application/json")
        
        #Then a 201 response is retrieved
        self.assertEqual("201 CREATED", result.status)
        #And the initial db count was incremented by 1
        self.assertEqual(initial_db_count + 1, ID.count())
        
        #And the data from db list model has the entry used on the end
        self.assertEqual({"id" : 1, "description" : descriptor, "data" : data_to_send["data"]}, ID.list()[-1])
                         
    def _integration_descriptor_add_400(self, descriptor, data_to_send):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.list()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = json.dumps(data_to_send),
                               content_type = "application/json")
        
        #Then a 400 Bad Request is retrieved
        self.assertEqual("400 BAD REQUEST", result.status)
        
        #And the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.list())
        
        #And the initial db count was not incremented
        self.assertEqual(initial_db_count, ID.count())
        
    def _integration_descriptor_add_404(self, descriptor, data_to_send):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.list()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = data_to_send,
                               content_type = "application/json")
        
        #Then a 404 Not Found is retrieved
        self.assertEqual("404 NOT FOUND", result.status)
        
        #And the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.list())
        
        #And the initial db count was not incremented
        self.assertEqual(initial_db_count, ID.count())
    
    def _integration_id_as_nan_404(self):
        #Given initial db count is recorded
        initial_db_count = ID.count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.list()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/right/left",
                               data = json.dumps("{}"),
                               content_type = "application/json")
        
        #Then a 404 Not Found is retrieved
        self.assertEqual("404 NOT FOUND", result.status)
        
        #And the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.list())
        
        #And the initial db count was not incremented
        self.assertEqual(initial_db_count, ID.count())