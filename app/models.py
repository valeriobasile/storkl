from app import db

class User(db.Model):
    username = db.Column(db.String(64), index = True, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
    projects = db.relationship('Project', backref = 'owns', lazy = 'dynamic')
    
    def __repr__(self):
        return '{0}'.format(self.username)

    def serialize(self):
        serialized = {'username' : self.username, 'email' : self.email}
        return serialized
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    owner = db.Column(db.String(64), db.ForeignKey('user.username'))
    description = db.Column(db.Text())
    created = db.Column(db.DateTime())

