from SuperDiffer.id.models import ID
from SuperDiffer import db

def count():
    return len(ID.query.all())
    
def list():
    data = ID.query.all()
    to_return = []
    for d in data:
        entry = {}
        entry["id"] = d.id
        entry["description"] = d.description.encode('utf-8','ignore')
        entry["data"] = d.data.encode('utf-8','ignore')
        to_return.append(entry)
    return to_return
    
def add(id, descriptor, data):
    try:
        u = ID(id = id, description = descriptor, data = data)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False
    return True
