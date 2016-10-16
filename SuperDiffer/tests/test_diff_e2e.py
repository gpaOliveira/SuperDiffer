from SuperDiffer.tests import *
from SuperDiffer.id import controllers as ID
from sqlalchemy import exc
import json
import base64
import os

class DiffE2ETestCases(SupperDifferBaseTestCase):
    """Test cases to verify if the endpoints can be used together safelly to load images as base64 values"""

    def _load_image_on_json(self, image_name):
        json_to_send = {"data":""}
        basedir = os.path.abspath(os.path.dirname(__file__))
        
        with open(basedir + os.sep + image_name, "rb") as image_file:
            json_to_send["data"] = base64.b64encode(image_file.read())
        
        return json_to_send
        
    def _post_on_descriptor(self, id, descriptor, data_to_send):
        result = self.app.post("/v1/diff/" + id + "/" + descriptor,
                               data = json.dumps(data_to_send),
                               content_type = "application/json")
        self.assertEqual("201 CREATED", result.status)
        
    def _get_diff(self, id):
        result = self.app.get("/v1/diff/" + id)
        self.assertEqual("200 OK", result.status)
        return json.loads(result.data)

    @groups(END_TO_END_TESTS_GROUP)
    def test_diff_e2e_lenna1_left_right(self):
        #Given Lenna1 is loaded on left and right
        data_to_post_left = self._load_image_on_json("Lenna.1.png")
        data_to_post_right = self._load_image_on_json("Lenna.1.png")
        self._post_on_descriptor("1", "left", data_to_post_left)
        self._post_on_descriptor("1", "right", data_to_post_right)
        
        #When the diff is returned
        response_diff_json = self._get_diff("1")
        
        #Then no difference is found
        self.assertEqual({"size":"equal", "diffs":[]}, response_diff_json)
        
    @groups(END_TO_END_TESTS_GROUP)
    def test_diff_e2e_lenna1_left_lenna2_right(self):
        #Given Lenna1 is loaded on left and right
        data_to_post_left = self._load_image_on_json("Lenna.1.png")
        data_to_post_right = self._load_image_on_json("Lenna.2.png")
        
        self._post_on_descriptor("1", "left", data_to_post_left)
        self._post_on_descriptor("1", "right", data_to_post_right)
        
        #When the diff is returned
        response_diff_json = self._get_diff("1")
        
        #Then no difference is found
        self.assertEqual({"size":"not equal", "diffs":[]}, response_diff_json)
