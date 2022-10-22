from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    Title = models.CharField(max_length=30)
    desc = models.TextField()
    file = models.FileField(default='',upload_to='static')

    def __str__(self):
        return self.Title
