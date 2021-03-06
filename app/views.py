from app import db, app, models, api
from utils import *
from flask import make_response, jsonify
from flask.ext import restful
from flask.ext.restful import abort, reqparse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

### User ###
class User(restful.Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username')
        self.parser.add_argument('email')

    def get(self, username):
        user = models.User.query.get(username)
        if user:
            return jsonify(user.serialize())
        else:
            abort(404, message="User {} doesn't exist".format(username))
            
    def post(self, username):
        args = self.parser.parse_args()
        try:
            new_user = models.User(username=args['username'], 
                 email=args['email'])
            db.session.add(new_user)
            db.session.commit()
            return 201
        except IntegrityError:
            abort(400, message="User {} already exists".format(args['username']))
            
    def delete(self, username):
        args = self.parser.parse_args()
        try:
            user = models.User.query.get(username)
            db.session.delete(user)
            db.session.commit()
            return 201
        except UnmappedInstanceError:
            abort(400, message="User {} does not exist".format('username'))
            
api.add_resource(User, '/u/<string:username>')


### User - owns - Project ###
class Ownership(restful.Resource):
    def get(self, username):
        projects = models.Project.query.filter_by(owner_id=username).all()
        return jsonify({ 'projects' : [p.serialize() for p in projects] })

api.add_resource(Ownership, '/u/<string:username>/owned')


### User - is in task comprised by - Project ###
class UserInvolvement(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        return jsonify({ 'projects' : [p.serialize() for p in user.involved()] })
        
api.add_resource(UserInvolvement, '/u/<string:username>/involved')


### User - Task ###
class Assignment(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        return jsonify({ 'tasks' : [t.serialize() for t in user.tasks] })

api.add_resource(Assignment, '/u/<string:username>/tasks')


### User - User ###
class Trust(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        return jsonify({ 'users' : [u.serialize() for u in user.trusted] })

api.add_resource(Trust, '/u/<string:username>/trusted')


### User - User ###
# every user involved in projects in which User is involved (minus himself)
class Association(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        associates = unique(flatten(p.involved() for p in user.involved()))
        
        associates.remove(user)
        return jsonify({ 'users' : [u.serialize() for u in associates] })
api.add_resource(Association, '/u/<string:username>/associated')


### Project ###
class Project(restful.Resource):
    def get(self,  project_id):
        project = models.Project.query.get(project_id)
        if not project:
            abort(404, message="Project {} doesn't exist".format(project_id))

        return jsonify(project.serialize())
        
api.add_resource(Project, '/p/<int:project_id>')


### Project - is in task comprised by - Project ###
class ProjectInvolvement(restful.Resource):
    def get(self, project_id):
        project = models.Project.query.get(project_id)
        return jsonify({ 'users' : [u.serialize() for u in project.involved()] })
api.add_resource(ProjectInvolvement, '/p/<int:project_id>/involved')


### Project - Task ###
class ProjectTasks(restful.Resource):
    def get(self, project_id):
        project = models.Project.query.get(project_id)
        return jsonify({ 'tasks' : [t.serialize() for t in project.tasks] })

api.add_resource(ProjectTasks, '/p/<int:project_id>/tasks')


### Task ###
class Task(restful.Resource):
    def get(self, task_id):
        task = models.Task.query.get(task_id)
        if not task:
            abort(404, message="Task {} doesn't exist".format(task_id))

        return jsonify(task.serialize())
        
api.add_resource(Task, '/t/<int:task_id>')


class Dependency(restful.Resource):
    def get(self, task_id):
        task = models.Task.query.get(task_id)
        if not task:
            abort(404, message="Task {} doesn't exist".format(task_id))

        return jsonify({'dependency': 
                         {'dependencies' : 
                            [t.serialize() for t in task.dependencies], 
                          'dependents' : 
                            [t.serialize() for t in task.dependents] }
                       })
        
api.add_resource(Dependency, '/t/<int:task_id>/dep')

# error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
    




