from SuperDiffer import app, db
from SuperDiffer.id import models as ID_models
import os.path
import unittest

_test_basedir = os.path.abspath(os.path.dirname(__file__))

class SupperDifferBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db_uri = 'sqlite:///' + os.path.join(_test_basedir, 'test.db')
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
#taken from https://github.com/valermor/nose2-tests-recipes
UNIT_TESTS_GROUP = 'UNIT_TESTS_GROUP'
INTEGRATON_TESTS_GROUP = 'INTEGRATON_TESTS_GROUP'
END_TO_END_TESTS_GROUP = 'END_TO_END_TESTS_GROUP'

def groups(*group_list):
    """Decorator that adds group name to test method for use with the attributes (-A) plugin.
    """
    def wrap_ob(ob):
        if len(group_list) == 1:
            setattr(ob, "group", group_list[0])
        elif len(group_list) > 1:
            setattr(ob, "groups", group_list)
        return ob
    return wrap_ob