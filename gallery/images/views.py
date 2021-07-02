from django.shortcuts import render
from .models import Images,Category,Location

# Create your views here.
def home(request):
    gallery = Images.objects.all()
    return render(request,'index.html',{'gallery':gallery})


def gallery(request):
    gallery = Images.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

    