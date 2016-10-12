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
