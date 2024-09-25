from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Dog
from .models import Breed 

# Dogs
from .serializers import DogSerializer

# Breeds
from .serializers import BreedSerializer


# Lets try ViewSets instead of snippets - Works
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from dogapi.serializers import DogSerializer


# Get Dog by ID  -- Works
@api_view(['GET'])
def rest_get_dog(request, dog_id):
    try:
        dog = Dog.objects.get(pk=dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found.'}, status=status.HTTP_404_NOT_FOUND)
    
# Get Breed by ID 
@api_view(['GET'])
def rest_get_breed(request, breed_id):
    try:
        breed = Breed.objects.get(pk=breed_id)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)
    except Breed.DoesNotExist:
        return Response({'error': 'Breed not found.'}, status=status.HTTP_404_NOT_FOUND)
    
# NEW #########################################################################################
# Viewset for dogs  
class DogViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)


# Viewset for breeds  
class BreedViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)
  
    def retrieve(self, request, pk=None):
        queryset = Breed.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(user)
        return Response(serializer.data)

