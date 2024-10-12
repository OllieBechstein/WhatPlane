from django.db import models

class Plane(models.Model):
    type = models.TextField()
    reg = models.TextField()
    captured = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
    class Meta:
        ordering = ['-captured']