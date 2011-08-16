from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(User)
	def __unicode__(self):
		return self.name
	
class Task(models.Model):
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project)
	deadline = models.DateTimeField(blank=True)
	users = models.ManyToManyField(User, blank=True)	
	dependency = models.ManyToManyField("self",blank=True)
	def __unicode__(self):
		return "{0}/{1}".format(self.project, self.name)
	
class Message(models.Model):
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User)
	Project = models.ForeignKey(Project)
	task = models.ForeignKey(Task, blank=True)
	def __unicode__(self):
		return "{0} - {1}: {2}...".format(self.timestamp, self.author, self.text[:50])
	
