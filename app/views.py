from app import app, models
from flask import make_response, jsonify

@app.route('/users')
def get_users():
    users = models.User.query.all()
    return jsonify({ 'users' : [u.serialize() for u in users] })

@app.route('/user/<string:username>')
def get_user(username):
    user = models.User.query.get(username)
    return jsonify(user.serialize())
    
#@app.route('/users')
#@app.route('/users')
#@app.route('/users')


# error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
