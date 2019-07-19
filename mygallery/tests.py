from django.test import TestCase
from .models import location, category, Image

# Create your tests here.
class locationTestClass(TestCase):
    def setUp(self):
        # Creating a new location and saving it
        self.location = location(name = 'Nairobi')
        self.location.save()
    
class categoryTestClass(TestCase):
    def setUp(self):
    # Creating a new category and saving it
        self.category = category(name = 'Testcategory')
        self.category.save()


class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.image= Image(image = "/images", name = "TestImage", description = "A image for testing", location =self.location, category="thrilling" )
        self.image.save_image()
        # Testing  instance

