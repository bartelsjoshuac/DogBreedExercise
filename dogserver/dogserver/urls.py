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

from rest_framework.routers import DefaultRouter

#urlpatterns = router.urls

# Gotta be a nicer way to work this back in....
adminpattern = [
    
    path('admin/', admin.site.urls),
]

urlpatterns = router.urls + adminpattern