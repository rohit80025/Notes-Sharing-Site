from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	contact = models.CharField(max_length=10,null=True)
	branch = models.CharField(max_length=50)
	role = models.CharField(max_length=20)


	def __self__(self):
		return self.user.username


class Notes(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	uploadingdate = models.CharField(max_length=30)
	branch = models.CharField(max_length=50)
	subject = models.CharField(max_length=30)
	notesfile = models.FileField(null=True)
	filetype = models.CharField(max_length=30,null=True)
	description = models.CharField(max_length=250,null=True)
	status = models.CharField(max_length=20)
    

	def __self__(self):
		return self.signup.user.username +" "+self.status