from SuperDiffer.id import models

def db_count():
    return len(models.ID.query.all())