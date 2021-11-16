from django.db import models
from author.models import Author

# Create your models here.
class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author_forien_id = models.ForeignKey(Author, on_delete=models.CASCADE,default=1)

