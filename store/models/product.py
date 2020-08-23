from django.db import models
from .category import Category

class Product1(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')


    @staticmethod
    def get_all_products():
        return Product1.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product1.objects.filter(category = category_id)
        else:
            return Product1.get_all_products()




