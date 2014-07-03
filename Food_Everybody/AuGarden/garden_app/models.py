from django.db import models

# Create your models here

class Garden(models.Model):
	City = models.CharField(max_length=100)
	State = models.CharField(max_length=100)
	Address = models.CharField(max_length=100)
	Garden_attendee = models.CharField(max_length=100)
	
class User(models.Model):
	First_name = models.CharField(max_length=100)
	Last_name = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
	State = models.CharField (max_length=100)
	Address = models.CharField (max_length=100)
	Garden_ID = models.ForeignKey(Garden)
	#This is how the user is connected to the garden. 
	Person_ID = models.CharField(max_length=100)

	def __unicode__(self):
		return self.First_name

class Produce(models.Model):
	Apples = models.BooleanField()
	Onions = models.BooleanField()
	Cilantro = models.BooleanField()
	Flowers = models.BooleanField()
	Garden_ID = models.ForeignKey(Garden)
	#This is how the produce is connected to the garden

