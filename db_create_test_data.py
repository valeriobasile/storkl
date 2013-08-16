from app import db, models
from datetime import datetime

# empty the db
for user in models.User.query.all():
    db.session.delete(user)
    
for projects in models.Project.query.all():
    db.session.delete(project)
db.session.commit()

u1 = models.User(username='john', email='john@email.com')
db.session.add(u1)

u2 = models.User(username='mary', email='mary@email.com')
db.session.add(u2)

p1 = models.Project(title='Hyperlamp ', owner='mary', description='A lamp shaped like an hypercube.', created=datetime.utcnow())
db.session.add(p1)
db.session.commit()

