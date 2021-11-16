from django.db import models

# Create your models here.
class Author(models.Model):
    auth_id = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.auth_name
