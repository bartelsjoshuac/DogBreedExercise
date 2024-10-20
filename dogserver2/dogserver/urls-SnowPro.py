from django.contrib import admin
from django.urls import path

# Dogs
from dogapi.views import rest_get_dog
from dogapi.views import DogViewSet

# Breeds (old)
from dogapi.views import rest_get_breed

# Using Viewsets
#from dogapi.views import breed_list

from dogapi.views import DogViewSet
from dogapi.views import BreedViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'api/dogs', DogViewSet, basename='dog')
router.register(r'api/breeds', BreedViewSet, basename='breed')
router.register(r'admin', admin.site,urls, basename=adm)

from rest_framework.routers import DefaultRouter

urlpatterns = router.urls

# Need to work my admin GUI into the router I guess?  I did try a few things with no luck
#urlpatterns = [
    
#    path('admin/', admin.site.urls),
#]

