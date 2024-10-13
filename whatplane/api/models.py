from django.db import models
from datetime import timedelta

class Plane(models.Model):
    type = models.TextField()
    reg = models.TextField(default='No Reg')
    captured = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type[0:50]
    
    class Meta:
        ordering = ['-captured']