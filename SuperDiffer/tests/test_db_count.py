from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID

class DBCountTestCase(SupperDifferBaseTestCase):
    def test_db_count_1(self):        
        #Given
        self.assertEqual(0, ID.db_count())
        
        #When
        u = ID_models.ID(id="1", left="a", right = "b")
        db.session.add(u)
        db.session.commit()
        
        #Then
        self.assertEqual(1, ID.db_count())