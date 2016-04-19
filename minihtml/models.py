from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.

class Post(models.Model):

	slug = models.SlugField(
			unique=True)
	website = models.URLField(
			max_length=2000)
	created_date = models.DateTimeField(
			default=timezone.now)
	tiny = models.CharField(
			max_length=2000)
	


	def __str__(self):
		return self.website
		