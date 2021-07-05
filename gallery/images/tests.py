from django.test import TestCase
from .models import Images,Category,Location

# Create your tests here.


class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='test_location')

    def save_location(self):
        self.location.save()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='music')

    def save_category(self):
        self.category.save()


class ImagesTestClass(TestCase):

    # #set up method
    def setUp(self):
        self.image=Images(name='happy',description="test_description",location=self.location,category=self.category,photo='img1')
    #testing instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images)) 
    #testing saving method
    def test_save_method(self):
        self.image.save_image()
        images=Images.objects.all()
        self.assertTrue(len(images)>0)

    def delete_image(self):
        self.image.delete()


