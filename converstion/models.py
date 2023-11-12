from django.db import models 
from django.contrib.auth.models import User
from item.models import Item

class Converstion(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='conversations')
    members = models.ManyToManyField(User, related_name='conversations')
    time = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified',)


class ConverstionMessage(models.Model):
    conversation = models.ForeignKey(Converstion, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_messages')

    class Meta:
        ordering = ('-time',)

