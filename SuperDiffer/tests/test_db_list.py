from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
import json

class DBListTestCase(SupperDifferBaseTestCase):

    @groups(UNIT_TESTS_GROUP)
    def test_db_list_1(self):        
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id="1", left="a", right = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then
        self.assertEqual([{"id" : 1, "left" : "a", "right" : "b"}], ID.db_list())

    @groups(INTEGRATON_TESTS_GROUP)
    def test_integration_db_list_1(self):
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id="1", left="a", right = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then
        result = self.app.get('/db_json_list') 
        self.assertEqual([{"id" : 1, "left" : "a", "right" : "b"}], json.loads(result.data))
