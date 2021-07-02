from django.shortcuts import render
from .models import Images,Category,Location

# Create your views here.
def home(request):
    
    return render(request,'index.html')


def gallery(request):
    gallery = Images.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

    