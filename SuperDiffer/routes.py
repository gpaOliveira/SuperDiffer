from SuperDiffer import app, db
from SuperDiffer.id import models as ID_models
from flask import Flask, render_template

@app.route('/db_count')
def db_count():
    data = ID_models.ID.query.all()
    return render_template("db.count.html", count=len(data))
    
@app.route('/')
def index():
    return 'Hello World!'
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
