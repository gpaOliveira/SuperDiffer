from SuperDiffer import app, db
from SuperDiffer.id import controllers as ID
import json
import pdb

from flask import Flask, render_template, request, abort

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
    if not ID.add_data(id, descriptor, data):
        abort(400)
    return "Created", 201
    
@app.route('/db_count')
def db_count():
    return render_template("db.count.html", count=ID.db_count())
    
@app.route('/db_json_list')
def db_list():
    return json.dumps(ID.db_list(), indent=6)
    
@app.route('/')
def index():
    return 'Hello World!'
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
