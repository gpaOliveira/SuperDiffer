from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
from sqlalchemy import exc
import json

class DBTestCases(SupperDifferBaseTestCase):
    """Test cases to verify and document the DB helpers behavior on the controller"""

    @groups(UNIT_TESTS_GROUP)
    def test_db_count_1(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When a data is added to the model
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then the database count is raised properlly by 1
        self.assertEqual(1, ID.count())

    @groups(UNIT_TESTS_GROUP)
    def test_db_count_2(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When two new different IDs are added to the model
        u = ID_models.ID(id = 1, description = "a", data = "b")
        db.session.add(u)
        u = ID_models.ID(id = 2, description = "a", data = "d")
        db.session.add(u)
        db.session.commit()
        
        #Then the database count is raised properlly by 2
        self.assertEqual(2, ID.count())
        
    @groups(UNIT_TESTS_GROUP)
    def test_db_count_non_unique_id(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When two new different descriptors for the ID are added to the model
        u = ID_models.ID(id=1, description="f", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then the database count is raised properlly by 2
        self.assertEqual(2, ID.count())
        
    @groups(UNIT_TESTS_GROUP)
    def test_db_count_unique_description_and_id(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When the same descriptor is added twice to an ID on the model
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        
        #Then an IntegrityError is raised and the database count is raised only by 1
        self.assertRaises(exc.IntegrityError, db.session.commit)
        db.session.rollback()
        self.assertEqual(1, ID.count())
        
    @groups(UNIT_TESTS_GROUP)
    def test_db_list_1(self):        
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When a data is added to the database model
        u = ID_models.ID(id="1", description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then a json representation of it is correctly returned
        self.assertEqual([{"id" : 1, "description" : "a", "data" : "b"}], ID.list())
    
    @groups(UNIT_TESTS_GROUP)
    def test_db_list_2_different_ids(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When two IDs are added to the database model
        u = ID_models.ID(id="1", description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id="2", description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then a json representation of them both is correctly returned
        self.assertEqual([{"id" : 1, "description" : "a", "data" : "b"}, 
                          {"id" : 2, "description" : "a", "data" : "b"}], 
                          ID.list())
                          
    @groups(UNIT_TESTS_GROUP)
    def test_db_list_2_different_descriptors(self):
        #Given no data is on the database
        self.assertEqual(0, ID.count())
        
        #When two descriptors are added to the database model bound to the same ID
        u = ID_models.ID(id="1", description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id="1", description="c", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then a json representation of them both is correctly returned
        self.assertEqual([{"id" : 1, "description" : "a", "data" : "b"}, 
                          {"id" : 1, "description" : "c", "data" : "b"}], 
                          ID.list())