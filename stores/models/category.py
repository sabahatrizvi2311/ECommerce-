from django.db import models

# Create your models here.

class Categorie(models.Model):
	title = models.CharField(max_length=150)
	subcategory = models.CharField(max_length=200)

	def __str__(self):
		return self.subcategory
