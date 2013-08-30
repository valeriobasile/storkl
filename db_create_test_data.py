from app import db, models, engine
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

# create the database
db.create_all()


# empty the db
for user in models.User.query.all():
    db.session.delete(user)
    
for project in models.Project.query.all():
    db.session.delete(project)
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
db.session.add(t1)


db.session.commit()


