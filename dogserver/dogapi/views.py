from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Dog
from .models import Breed

from .serializers import DogSerializer
from .serializers import BreedSerializer

@api_view(['GET'])
def rest_get_dog(request, dog_id):
    try:
        dog = Dog.objects.get(pk=dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found.'}, status=status.HTTP_404_NOT_FOUND)
    
 # My Breed View 
@api_view(['GET'])
def rest_get_breed(request, breed_id):
    try:
        breed = Breed.objects.get(pk=breed_id)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)
    except Breed.DoesNotExist:
        return Response({'error': 'Breed not found.'}, status=status.HTTP_404_NOT_FOUND)   