from app import db

class User(db.Model):
    username = db.Column(db.String(64), index = True, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
    projects = db.relationship('Project', backref = 'owns', lazy = 'dynamic')
    
    def serialize(self):
        serialized = {'username' : self.username, 
                      'email' : self.email}
        return serialized
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    owner = db.Column(db.String(64), db.ForeignKey('user.username'))
    description = db.Column(db.Text())
    created = db.Column(db.DateTime())
    tasks = db.relationship('Task', backref = 'include', lazy = 'dynamic')
    
    def serialize(self):
        user = User.query.get(self.owner)
        serialized = {'title' : self.title, 
                      'owner' : user.serialize(), 
                      'description' : self.description, 
                      'created' : self.created}
        return serialized

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    project = db.Column(db.Integer, db.ForeignKey('project.id'))
    name = db.Column(db.String(64))
    description = db.Column(db.Text())

    def serialize(self):
        project = Project.query.get(self.project)
        serialized = {'name' : self.name, 
                      'project' : project.serialize(), 
                      'description' : self.description}
        return serialized


