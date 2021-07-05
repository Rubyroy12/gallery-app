from django.test import TestCase
from .models import Images,Category,Location

# Create your tests here.
class ImagesTestClass(TestCase):
    #set up method
    def setUp(self):
        self.james=Images(name='happy',description="test_description",location='ainamoi',category='music',photo='img1')
    #testing instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Images)) 
    #testing saving method
    def test_save_method(self):
        self.james.save_editor()
        editors=Images.objects.all()
        self.assertTrue(len(editors)>0)