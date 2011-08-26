from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	owner = models.ForeignKey(User)
	def __unicode__(self):
		return self.name

	
class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	project = models.ForeignKey(Project)
	deadline = models.DateField(default=None, null=True, blank=True)
	users = models.ManyToManyField(User, blank=True)	
	dependencies = models.ManyToManyField("self", symmetrical=False, blank=True)
	completed = models.BooleanField(default=False)
	def __unicode__(self):
		return "{0}".format(self.name)
	
class Message(models.Model):
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	task = models.ForeignKey(Task, blank=True)
	def __unicode__(self):
		return "{0} - {1}: {2}...".format(self.timestamp, self.author, self.text[:50])
	
