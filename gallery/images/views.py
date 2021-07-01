from django.shortcuts import render
from .models import Images,Category,Location

# Create your views here.
def home(request):
    images = Images.get_image()
    return render(request,'index.html',{'images':images})