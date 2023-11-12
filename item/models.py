from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='items' ,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name