from django.db import models

class Member(models.Model):
	name = models.CharField(max_length = 200)
	sex = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 200)
	password = models.CharField(max_length = 200)
	mobile_number = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.name
	
class Property(models.Model):
	member = models.ForeignKey('Member',on_delete = models.CASCADE)
	nameOfProperty = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.nameOfProperty
