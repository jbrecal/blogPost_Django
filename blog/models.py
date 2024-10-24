from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'Draft'),(1, 'Publish')) 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # text field is the format of a string
    date_created = models.DateTimeField(auto_now_add=True) # auto_now_add will set the date created to the time of creation
    slug = models.SlugField(max_length=200, unique=True) # unique will ensure that no two posts have the same slug
    author = models.ForeignKey(to=User, on_delete=models.CASCADE) # on_delete will delete the  user post if the user is deleted
    status = models.IntegerField(choices=STATUS, default=0) # default will set the status to draft
    
    def __str__(self):  # __str__ will return the title is better represented in the admin panel
        return self.title