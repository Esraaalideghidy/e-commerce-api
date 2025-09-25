
import uuid
from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    title=models.CharField(max_length=100)
    description=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    name=models.CharField(max_length=100)
    

    def __str__(self):
        return f'Review for {self.product.title}'



