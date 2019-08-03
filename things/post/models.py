from django.db import models

class ThingManager(models.Manager):
	def posts(self):
		return self.order_by('-id')

class Thing(models.Model):
	text = models.TextField(default=" ")
	objects = ThingManager()
	
	def __str__(self):
		return self.text