"""
URL configuration for dogserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Dogs
from dogapi.views import rest_get_dog
from dogapi.views import DogViewSet

# Breeds
from dogapi.views import rest_get_breed

# Using Viewsets
from dogapi.views import dog_list
from dogapi.views import breed_list

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    # My dog thing from an older lab
    path('rest/dog/<int:dog_id>/', rest_get_dog, name='rest_get_dog'),

    #### Dogs
    # This gets us all dogs
    path('api/dogs/', dog_list, name='dog_list'),
    # This gets us a dog by ID
    path('api/dogs/<int:dog_id>/', rest_get_dog, name='rest_get_dog'),

    ### Breeds
    # This gets us all breeds
    path('api/breeds/', breed_list, name='breed_list'),
    # This gets a breed by ID
    path('api/breeds/<int:breed_id>/', rest_get_breed, name='rest_get_breed'),
]

