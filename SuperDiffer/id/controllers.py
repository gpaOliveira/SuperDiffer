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

def _grab_descriptors_values_to_diff(id_to_diff, descriptors_to_diff):
    """"Grab all the descriptors values to diff or get out"""
    to_diff = {}
    for d in descriptors_to_diff:
        value = ID.query.filter_by(id = id_to_diff, description = d).first()
        if value:
            to_diff[d] = value
        else:
            return None
    return to_diff
    
def diff(id_to_diff, descriptors_to_diff):
    to_diff = _grab_descriptors_values_to_diff(id_to_diff, descriptors_to_diff)
    diff = {}
    if not to_diff:
        return None        
    
    return diff