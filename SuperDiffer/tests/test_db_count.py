from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
from sqlite3 import IntegrityError
from sqlalchemy import exc

class DBCountTestCase(SupperDifferBaseTestCase):
    
    @groups(UNIT_TESTS_GROUP)
    def test_db_count_1(self):
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then
        self.assertEqual(1, ID.db_count())

    @groups(UNIT_TESTS_GROUP)
    def test_db_count_2(self):
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id = 1, description = "a", data = "b")
        db.session.add(u)
        u = ID_models.ID(id = 2, description = "a", data = "d")
        db.session.add(u)
        db.session.commit()
        
        #Then
        self.assertEqual(2, ID.db_count())
        
    @groups(UNIT_TESTS_GROUP)
    def test_db_count_non_unique_id(self):
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id=1, description="f", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then
        self.assertEqual(2, ID.db_count())
        
    @groups(UNIT_TESTS_GROUP)
    def test_db_count_unique_description_and_id(self):
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        db.session.commit()
        u = ID_models.ID(id=1, description="a", data = "b")
        db.session.add(u)
        
        #Then
        self.assertRaises(exc.IntegrityError, db.session.commit)
        db.session.rollback()
        self.assertEqual(1, ID.db_count())