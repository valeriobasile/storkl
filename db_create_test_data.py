from app import db, models
from datetime import datetime


# create the database
db.create_all()


# empty the db
for user in models.User.query.all():
    db.session.delete(user)
    
for project in models.Project.query.all():
    db.session.delete(project)

for task in models.Task.query.all():
    db.session.delete(task)

db.session.commit()

u1 = models.User(username='john', 
                 email='john@email.com')
db.session.add(u1)

u2 = models.User(username='mary', 
                 email='mary@email.com')
db.session.add(u2)

p1 = models.Project(id=1, 
                    title='Hyperlamp', 
                    owner_id='mary', 
                    description='A lamp shaped like an hypercube.', 
                    created=datetime.utcnow())
db.session.add(p1)

t1 = models.Task(id=1,
                 project_id=1, 
                 name='Buy wooden sticks', 
                 description='go to Gamma and buy a few meters of thin cut wood.',
                 users=[u1])

t2 = models.Task(id=2,
                 project_id=1, 
                 name='Buy paper', 
                 description='go to the store and buy a few square meters of multi-color paper.',
                 users=[u1, u2])
db.session.add(t1)


db.session.commit()

