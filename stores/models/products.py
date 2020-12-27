from django.db import models
from .category import Categorie

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500, default="", null=True)
	category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to='static/images/')
	image2 = models.ImageField(upload_to='static/images/', null=True, default="")
	image3 = models.ImageField(upload_to='static/images/', null=True, default="")

	@staticmethod
	def get_all_products_by_categoryid(category_id):
		if category_id:
			return Product.objects.filter(category=category_id)
		else:
			return Product.objects.all()