from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

class Plane(models.Model):
    type = models.TextField()
    reg = models.TextField(default='No Reg')
    captured = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type[0:50]
    
    class Meta:
        ordering = ['-captured']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    planes = models.ManyToManyField('Plane', related_name='owners')
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username