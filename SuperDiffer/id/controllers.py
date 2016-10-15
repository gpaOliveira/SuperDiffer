from SuperDiffer.id import models
from SuperDiffer import db

def db_count():
    return len(models.ID.query.all())
    
def db_list():
    data = models.ID.query.all()
    to_return = []
    for d in data:
        entry = {}
        entry["id"] = d.id
        entry["description"] = d.description.encode('utf-8','ignore')
        entry["data"] = d.data.encode('utf-8','ignore')
        to_return.append(entry)
    return to_return
    
def add_data(id, descriptor, data):
    try:
        u = models.ID(id = id, description = descriptor, data = data)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False
    return True