from django.db import models

# Create your models here.
class location(models.Model):
    '''
    This is a class for the location of where the images were taken
    '''
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class category(models.Model):
    '''
    This is a class for the different categories that different images belong to
    '''
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class Image(models.Model):
    '''
    image class for all images added to the application
    '''
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category)
    location = models.ForeignKey(location)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

