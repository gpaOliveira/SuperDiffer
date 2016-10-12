from SuperDiffer import app, db
from SuperDiffer.id import controllers as ID
import json

from flask import Flask, render_template

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
