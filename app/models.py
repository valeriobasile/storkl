from app import db, engine

assignment = db.Table('assignment',
    db.Column('user', db.String(64), db.ForeignKey('user.username')),
    db.Column('task', db.Integer, db.ForeignKey('task.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(64), index = True, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
#    projects = db.relationship('Project', backref = 'owner', lazy = 'dynamic')
#    tasks = db.relationship('Task', secondary=assignment, backref=db.backref('user', lazy='dynamic'))
    def serialize(self):
        serialized = {'username' : self.username, 
                      'email' : self.email}
        return serialized


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    owner_id = db.Column(db.String(64), db.ForeignKey('user.username'))
    description = db.Column(db.Text())
    created = db.Column(db.DateTime())
    tasks = db.relationship('Task', backref = 'project', lazy = 'dynamic')
    
    def serialize(self):
        user = User.query.get(self.owner_id)
        serialized = {'title' : self.title, 
                      'owner' : user.serialize(), 
                      'description' : self.description, 
                      'created' : self.created}
        return serialized



class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    name = db.Column(db.String(64))
    description = db.Column(db.Text())
    users = db.relationship('User', secondary=assignment, backref=db.backref('task', lazy='dynamic'))

    def serialize(self):
        project = Project.query.get(self.project_id)
        serialized = {'name' : self.name, 
                      'project' : project.serialize(), 
                      'description' : self.description}
        return serialized



