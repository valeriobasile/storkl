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
        projects = models.Project.query.filter_by(owner=username).all()
        return jsonify({ 'projects' : [p.serialize() for p in projects] })

api.add_resource(Ownership, '/u/<string:username>/owns')


### Project ###
class Project(restful.Resource):
    def get(self,  project_id):
        project = models.Project.query.get(project_id)
        if not project:
            abort(404, message="Project {} doesn't exist".format(project_id))

        return jsonify(project.serialize())
        
api.add_resource(Project, '/p/<int:project_id>')


### User - is in task comprised by - Project ###
class Involvement(restful.Resource):
    def get(self, username):
        projects = models.Project.query.filter_by(owner=username).all()
        return jsonify({ 'projects' : [p.serialize() for p in projects] })

api.add_resource(Involvement, '/u/<string:username>/involved')


### Task ###
class Task(restful.Resource):
    def get(self, task_id):
        task = models.Task.query.get(task_id)
        if not task:
            abort(404, message="Task {} doesn't exist".format(task_id))

        return jsonify(task.serialize())
        
api.add_resource(Task, '/t/<int:task_id>')


### User - Task ###
class Assignment(restful.Resource):
    def get(self, username):
        user = models.User.query.get(username)
        return jsonify({ 'tasks' : [t.serialize() for t in user.assignment] })

api.add_resource(Assignment, '/u/<string:username>/assigned')



# error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
    




