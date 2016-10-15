from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
import json

class SupperDifferBaseDescriptortTestCase(SupperDifferBaseTestCase):

    def _descriptor_add_ok(self, descriptor):
        #Given initial db count is recorded
        initial_db_count = ID.db_count()
        
        #When a model entry is added
        model_entry_status = ID.add_data(1, descriptor, "abc")
        
        #Then the model entry status is ok
        self.assertEqual(True, model_entry_status)
        
        #And the initial db count was incremented by 1
        self.assertEqual(initial_db_count + 1, ID.db_count())
        
        #And the data from db list model has the entry as used in the end
        self.assertEqual({"id" : 1, "description" : descriptor, "data" : "abc"}, ID.db_list()[-1])        
        
    def _descriptor_add_not_ok(self, descriptor):
        #Given initial db count is recorded
        initial_db_count = ID.db_count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.db_list()
        
        #When a model entry is added
        model_entry_status = ID.add_data(1, descriptor, "abc")
        
        #Then the model entry status is not ok
        self.assertEqual(False, model_entry_status)
        
        #Then the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.db_list())
        
        #And the initial db count is the same as the beggining
        self.assertEqual(initial_db_count, ID.db_count())

    def _integration_descriptor_add_201(self, descriptor, data_to_send):
        #Given initial db count is recorded
        initial_db_count = ID.db_count()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = data_to_send,
                               content_type = "application/json")
        
        #Then a 201 response is retrieved
        self.assertEqual("201 CREATED", result.status)
        #And the initial db count was incremented by 1
        self.assertEqual(initial_db_count + 1, ID.db_count())
        
        #And the data from db list model has the entry used on the end
        self.assertEqual({"id" : 1, "description" : descriptor, "data" : data_to_send}, ID.db_list()[-1])
                         
    def _integration_descriptor_add_400(self, descriptor, data_to_send):
        #Given initial db count is recorded
        initial_db_count = ID.db_count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.db_list()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = data_to_send,
                               content_type = "application/json")
        
        #Then a 400 Bad Request is retrieved
        self.assertEqual("400 BAD REQUEST", result.status)
        
        #And the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.db_list())
        
        #And the initial db count was not incremented
        self.assertEqual(initial_db_count, ID.db_count())
        
    def _integration_descriptor_add_404(self, descriptor, data_to_send):
        #Given initial db count is recorded
        initial_db_count = ID.db_count()
        
        #And initial db list data is recorded
        initial_db_list_data = ID.db_list()
        
        #When a request is made to add a certain description
        result = self.app.post("/v1/diff/1/" + descriptor,
                               data = data_to_send,
                               content_type = "application/json")
        
        #Then a 404 Not Found is retrieved
        self.assertEqual("404 NOT FOUND", result.status)
        
        #And the data from db list model is the same as the beggining
        self.assertEqual(initial_db_list_data, ID.db_list())
        
        #And the initial db count was not incremented
        self.assertEqual(initial_db_count, ID.db_count())
