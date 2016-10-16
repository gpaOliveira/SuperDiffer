from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
from sqlalchemy import exc
import json

class DiffTestCases(SupperDifferBaseTestCase):

    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_any_descriptors(self):
        #When
        self.assertEqual(0, ID.count())
        u = ID_models.ID(id = 1, description = "a", data = "b")
        db.session.add(u)
        db.session.commit()

        #Then
        self.assertEqual(None, ID.diff(1, []))
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_all_descriptors(self):
        #When
        self.assertEqual(0, ID.count())
        u = ID_models.ID(id = 1, description = "a", data = "b")
        db.session.add(u)
        db.session.commit()

        #Then
        self.assertEqual(None, ID.diff(1, ["a","b"]))
        
    @groups(UNIT_TESTS_GROUP)
    def test_diff_without_id(self):
        #When
        self.assertEqual(0, ID.count())
        u = ID_models.ID(id = 1, description = "a", data = "b")
        db.session.add(u)
        db.session.commit()

        #Then
        self.assertEqual(None, ID.diff(2, ["a"]))
        
    @groups(INTEGRATON_TESTS_GROUP)
    def test_diff_integration_bad_descriptors(self):
        #Given Left description of ID = 1 is added
        self.assertEqual(True, ID.add(1, "left", "abcd"))
        self.assertEqual(1, ID.count())
        initial_id_list = ID.list()
        
        #When a diff is made asking for left and right of ID = 1
        result = self.app.get("/v1/diff/1")
        
        #Then a 400 Bad Request is retrieved
        self.assertEqual("400 BAD REQUEST", result.status)
        
        #And nothing changed on the databse
        self.assertEqual(initial_id_list, ID.list())