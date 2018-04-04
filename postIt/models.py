from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	userName	=models.CharField(max_length=200)
	Category	=models.CharField(max_length=200)
	Title		=models.CharField(max_length=200)
	Content		=models.CharField(max_length=200)
	Private		=models.CharField(max_length=20)
	comingNext	=models.CharField(max_length=100,null=True,blank=True)
	pub_date	=models.DateTimeField('Publish Date')
	def __str__(self):
		return self.userName
	def was_published_recently(self):
		return self.pub_date>=timezone.now()-timedelta(days=1)	
