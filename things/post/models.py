from django.db import models

from django.contrib.auth.models import User  

class ThingManager(models.Manager):
	def posts(self):
		return self.order_by('-id')

class Thing(models.Model):
	text = models.TextField(default=" ")
	author = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
	public = models.BooleanField(default=False)
	objects = ThingManager()
	
	def __str__(self):
		return self.text