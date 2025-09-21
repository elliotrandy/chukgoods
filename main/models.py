import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('apparel', 'Apparel'),
        ('footwear', 'Footwear'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('fan gear', 'Fan Gear'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    # @property
    # def is_product_hot(self):
    #     return self.product_views > 20
        
    # def increment_views(self):
    #     self.product_views += 1
    #     self.save()