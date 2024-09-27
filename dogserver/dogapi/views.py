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


# A bunch of stuff for other viewset types to try
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets


############################################### OLD CODE from other labs ##############################
# Get Dog by ID 
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
    
###################################################################################################
# Note I used HTTP_417_EXPECTATION_FAILED in debuging vs. 404, as when I was calling /dog/# I would get 404 for the dog if it was already gone 
# and this made it is easier to differentiate if it was my code or if I need to make more dogs and bredes 

# Viewset for dogs  

##### Looks good!!!!
class DogViewSet(ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
#######

    #### Get list of all dogs
    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create a new dog
    def create(self, request):    
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'This should have created a dog but did not but failed .'}, status=status.HTTP_417_EXPECTATION_FAILED)
    
    # Retrive a dog by ID
    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        dog = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    
    # This updates a dog by ID
    def update(self, request, pk=None):
        queryset = Dog.objects.all()
        dog = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'This should have updated a dog by ID but failed.'}, status=status.HTTP_417_EXPECTATION_FAILED)
    
    # This deletes a dog
    def destroy(self, request, pk=None):
        queryset = Dog.objects.all()
        dog = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(dog)
        dog.delete()
        return Response({'success': 'This deleted a dog.'}, status=status.HTTP_200_OK)




# Viewset for breeds  
class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    
    #### Get list of all breeds 
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # Create a new breed
    def create(self, request):    
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'This should have created a breed but did not, but failed.'}, status=status.HTTP_417_EXPECTATION_FAILED)

    # Retrieve a breed by ID
    def retrieve(self, request, pk=None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)
    
    # This updates a breed by ID
    def update(self, request, pk=None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'This should have updated a breed by ID but failed.'}, status=status.HTTP_417_EXPECTATION_FAILED)
    
    # This deletes a breed
    def destroy(self, request, pk=None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(breed)
        breed.delete()
        return Response({'success': 'This deleted a breed.'}, status=status.HTTP_200_OK)