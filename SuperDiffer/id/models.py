from SuperDiffer import db

class ID(db.Model):
    __tablename__ = "ID"
    id = db.Column(db.Integer, primary_key=True)
    left = db.Column(db.String(120))
    right = db.Column(db.String(120))
    
    def __init__(self, id=None, left=None, right=None):
      self.id = id
      self.left = left
      self.right = right
      
    def __repr__(self):
        return "<ID {0}>\n\tLeft = {1}\n\tRight = {2}".format(self.id, self.left, self.right)