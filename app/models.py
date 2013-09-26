from app import db
<<<<<<< HEAD
from app.utils import *

=======
    
>>>>>>> 6a80fd0f3a41b8dcbfba3b8c990f26f082540d20
assignment = db.Table('assignment',
    db.Column('user', db.String(64), db.ForeignKey('user.username')),
    db.Column('task', db.Integer, db.ForeignKey('task.id'))
)

<<<<<<< HEAD
trust = db.Table('trust',
    db.Column('trustee', db.String(64), db.ForeignKey('user.username'), primary_key=True),
    db.Column('trusted', db.String(64), db.ForeignKey('user.username'), primary_key=True)
)

dependency = db.Table('dependency',
    db.Column('depender', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('dependent', db.Integer, db.ForeignKey('task.id'), primary_key=True)
=======
dependency = db.Table('dependency',
    db.Column('master', db.Integer, db.ForeignKey('task.id')),
    db.Column('slave', db.Integer, db.ForeignKey('task.id'))
>>>>>>> 6a80fd0f3a41b8dcbfba3b8c990f26f082540d20
)

class User(db.Model):
    username = db.Column(db.String(64), index = True, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
    projects = db.relationship('Project', backref = 'owner', lazy = 'dynamic')
    tasks = db.relationship('Task', 
                            secondary=assignment, 
                            backref=db.backref('user', 
                                               lazy='dynamic'))
    trusted = db.relationship('User', 
                              secondary=trust, 
                              backref=db.backref('trustees'), 
                              lazy='dynamic',
                              primaryjoin=username==trust.c.trustee,
                              secondaryjoin=username==trust.c.trusted)
    
    def involved(self):
        return list(set([task.project for task in self.tasks]))
    
    def serialize(self):
        serialized = {'username' : self.username, 
                      'email' : self.email}
        return serialized


class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    owner_id = db.Column(db.String(64), db.ForeignKey('user.username'))
    description = db.Column(db.Text())
    created = db.Column(db.DateTime())
    tasks = db.relationship('Task', backref = 'project', lazy = 'dynamic')
    
    def involved(self):
        return unique(flatten([task.users for task in self.tasks]))
        
        return list(set([
            val for subl in [
                task.users for task in self.tasks
            ] for val in subl
        ]))
        
    def serialize(self):
        user = User.query.get(self.owner_id)
        serialized = {'title' : self.title, 
                      'owner' : user.serialize(), 
                      'description' : self.description, 
                      'created' : self.created}
        return serialized



class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    name = db.Column(db.String(64))
    description = db.Column(db.Text())
    users = db.relationship('User', secondary=assignment, backref=db.backref('task', lazy='dynamic'))
<<<<<<< HEAD
    tasks = db.relationship('Task', secondary=dependency, backref=db.backref('depender', lazy='dynamic'))
    dependents = db.relationship('Task', 
                              secondary=dependency, 
                              backref=db.backref('dependers'), 
                              lazy='dynamic',
                              primaryjoin=id==dependency.c.dependent,
                              secondaryjoin=id==dependency.c.depender)
     
=======
    dependencies = db.relationship('Task', secondary=dependency, primaryjoin=dependency.c.slave==id, secondaryjoin=dependency.c.master==id, backref='dependent')
    dependents = db.relationship('Task', secondary=dependency, primaryjoin=dependency.c.master==id, secondaryjoin=dependency.c.slave==id, backref='dependency')

>>>>>>> 6a80fd0f3a41b8dcbfba3b8c990f26f082540d20
    def serialize(self):
        project = Project.query.get(self.project_id)
        serialized = {'name' : self.name, 
                      'project' : project.serialize(), 
                      'description' : self.description}
        return serialized


