from SuperDiffer import app, db
from SuperDiffer.id import controllers as ID
import json
import pdb

from flask import Flask, render_template, request, abort

#References: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

@app.route('/v1/diff/<int:id>', methods=['GET'])
def diff_right_left(id):
    diff = ID.diff(id, ["left","right"])
    if not diff:
        abort(400)
        
    return json.dumps(diff)

@app.route('/v1/diff/<int:id>/left', methods=['POST'])
def add_left_to_id(id):
    return _add_data_to_id_description(id, "left", request.json)
    
@app.route('/v1/diff/<int:id>/right', methods=['POST'])
def add_right_to_id(id):
    return _add_data_to_id_description(id, "right", request.json)

def _add_data_to_id_description(id, descriptor, request_json):
    #pdb.set_trace()
    try:
        data = json.dumps(request_json)#remove unicode data received
    except ValueError:
        abort(400)
    if not ID.add(id, descriptor, data):
        abort(400)
    return "Created", 201
   
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
