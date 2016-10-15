from SuperDiffer import db

class ID(db.Model):
    __tablename__ = "ID"
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(60), primary_key = True)
    data = db.Column(db.String(360))
    
    def __init__(self, id=None, description=None, data=None):
      self.id = id
      self.description = description
      self.data = data
      
    def __repr__(self):
        return "<ID {0}>\n\tDescription = {1}\n\tData = {2}".format(self.id, self.description, self.data)