from app import app, models, api
from flask import make_response, jsonify
from flask.ext import restful
from flask.ext.restful import abort

### User ###
class User(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        if user:
            return jsonify(user.serialize())
        else:
            abort(404, message="User {} doesn't exist".format(username))
            
api.add_resource(User, '/u/<string:username>')


### User - owns - Project ###
class Ownership(restful.Resource):
    def get(self, username):
        projects = models.Project.query.filter_by(owner_id=username).all()
        return jsonify({ 'projects' : [p.serialize() for p in projects] })

api.add_resource(Ownership, '/u/<string:username>/owns')


### User - is in task comprised by - Project ###
class UserInvolvement(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        projects = list(set([task.project for task in user.tasks]))
        return jsonify({ 'projects' : [p.serialize() for p in projects] })

api.add_resource(UserInvolvement, '/u/<string:username>/involved')


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
        users = list(set([val for subl in [task.users for task in project.tasks] for val in subl]))
        return jsonify({ 'users' : [u.serialize() for u in users] })

api.add_resource(ProjectInvolvement, '/p/<int:project_id>/involved')


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


### User - Task ###
class Assignment(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        return jsonify({ 'tasks' : [t.serialize() for t in user.tasks] })

api.add_resource(Assignment, '/u/<string:username>/assigned')



# error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
    




