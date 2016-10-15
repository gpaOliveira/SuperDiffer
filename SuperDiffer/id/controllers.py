from SuperDiffer.id import models

def db_count():
    return len(models.ID.query.all())
    
def db_list():
    data = models.ID.query.all()
    to_return = []
    for d in data:
        entry = {}
        entry["id"] = d.id
        entry["description"] = d.description.encode('ascii','ignore')
        entry["data"] = d.data.encode('ascii','ignore')
        to_return.append(entry)
    return to_return