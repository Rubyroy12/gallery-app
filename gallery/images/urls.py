from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    url('^$', views.home, name='homepage'),
    url('^gallery/', views.gallery, name='gallery'),
    url('^gallery/<int:image_id>/$', views.single_image, name='image_details'),
    url(r'^gallery/$',views.technology, name='technology'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
