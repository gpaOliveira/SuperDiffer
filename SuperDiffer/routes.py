from SuperDiffer import app, db
from SuperDiffer.id import controllers as ID
from flask import Flask, render_template, request, abort, jsonify
import json,base64,pdb

"""Routes to allow clients to add left and right base64 encoded on JSON values and fetch their diff"""

#References: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

@app.route('/v1/diff/<int:id>', methods=['GET'])
def diff_right_left(id):
    """Calculates the diff between left and right descriptors of a given ID"""
    all_diff_data = ID.diff(id, ["left","right"])
    if not all_diff_data or not all_diff_data["left_right"]:
        abort(400)        
    return jsonify(all_diff_data["left_right"])

@app.route('/v1/diff/<int:id>/left', methods=['POST'])
def add_left_to_id(id):
    """Add a JSON base64 value (in the format: {"data":"base64value"}) to the left descriptor of a given ID"""
    return _add_data_to_id_description(id, "left", request.json)
    
@app.route('/v1/diff/<int:id>/right', methods=['POST'])
def add_right_to_id(id):
    """Add a JSON base64 value (in the format: {"data":"base64value"}) to the right descriptor of a given ID"""
    return _add_data_to_id_description(id, "right", request.json)

def _is_base64(value):
    """Returns true only if value only has base64 chars (A-Z,a-z,0-9,+ or /)"""
    #http://stackoverflow.com/questions/12315398/verify-is-a-string-is-encoded-in-base64-python
    try:
        enc = base64.b64encode(base64.b64decode(value)).strip()
        return enc == value
    except TypeError:
        return False
    
def _add_data_to_id_description(id, descriptor, request_json):
    """Add a base64 value obtained from a JSON in the format {"data":"base64value"}) to the given descriptor of a given ID"""
    if not "data" in request_json:# no data key on json ? abort !
        abort(400)
    try:#arrays or other objects that doesnt have encode methods should not be accepted - abort !
        no_unicode_data = request_json["data"].encode("utf-8")
    except:
        abort(400)
    if not _is_base64(no_unicode_data):# no base64 value on data key ? abort !
        abort(400)
    if not ID.add(id, descriptor, no_unicode_data):# add failed due to some database problem ? yeah, abort !
        abort(400)
    return "Created", 201 #yey!
   
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
