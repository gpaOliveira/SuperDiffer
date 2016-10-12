from SuperDiffer import app, db
from SuperDiffer.id import controllers as ID

from flask import Flask, render_template

@app.route('/db_count')
def db_count():
    return render_template("db.count.html", count=ID.db_count())
    
@app.route('/')
def index():
    return 'Hello World!'
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
