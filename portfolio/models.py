import imp
from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Blogs(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=400)
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	summary = models.TextField(null=True, blank=True)
	desc  = RichTextField()
	

	def __str__(self):
		return self.title

class Portfolio(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=400)
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	summary = models.TextField(null=True, blank=True)
	desc  = RichTextField()
	url = models.URLField( blank=True, null=True)

	def __str__(self):
		return self.title