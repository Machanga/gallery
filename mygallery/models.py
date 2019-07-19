from django.db import models

# Create your models here.
class Image(models.Model):
    '''
    image Class for all images added to the application
    '''
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(category)
    location = models.ForeignKey(location)