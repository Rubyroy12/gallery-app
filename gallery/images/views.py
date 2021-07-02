from django.shortcuts import render,redirect
from .models import Images,Category,Location
from django.http import Http404

# Create your views here.
def home(request):
    
    return render(request,'index.html')


def gallery(request):
    gallery = Images.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def single_image(request,image_id):
    try:
        image = Images.objects.get(id=image_id)
    except DoesNotExist:
        Http404()
    
    return render(request,'single_image.html',{'image':image})
    
    


