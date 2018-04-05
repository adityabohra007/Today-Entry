from django.db import models
from django.utils import timezone
from today import settings
from django.contrib.auth.models import AbstractUser
# Post models here.
class Post(models.Model):
	userName	=models.CharField(max_length=200)
	Category	=models.CharField(max_length=200)
	Title		=models.CharField(max_length=200)
	Content		=models.CharField(max_length=200)
	Private		=models.CharField(max_length=20)
	#comingNext	=models.CharField(max_length=100,null=True,blank=True)
	pub_date	=models.DateTimeField('Publish Date',default=timezone.now)
	def __str__(self):
		return self.userName
	def was_published_recently(self):
		return self.pub_date>=timezone.now()-timedelta(days=1)	




# User models here.
class CustomUser(AbstractUser):
	name=models.CharField(blank=True,max_length=225)
	def __str__(self):
		return self.email