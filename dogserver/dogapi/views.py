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

# Viewset for dogs  

#####Looks good!!!!
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
            return Response({'success': 'This  created a dog.'}, status=status.HTTP_200_OK)
        return Response({'success': 'This should have created a dog but did not .'}, status=status.HTTP_200_OK)
    
    # Retrive a dog by ID
    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
    
    # Needs to update a dog by ID
    def update(self, request, pk=None):
        return Response({'success': 'This would update a dog by ID.'}, status=status.HTTP_200_OK)
    
    # This deletes a dog
    def destroy(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        user.delete()
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
            return Response({'success': 'This  created a breed.'}, status=status.HTTP_200_OK)
        return Response({'success': 'This should have created a breed but did not .'}, status=status.HTTP_200_OK)

    # Retrieve a breed by ID
    def retrieve(self, request, pk=None):
        queryset = Breed.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(user)
        return Response(serializer.data)
    
    # Needs to update a breed by ID
    def update(self, request, pk=None):
        return Response({'success': 'This would update a breed by ID.'}, status=status.HTTP_200_OK)
    
    # This deletes a breed
    def destroy(self, request, pk=None):
        queryset = Breed.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(user)
        user.delete()
        return Response({'success': 'This deleted a breed.'}, status=status.HTTP_200_OK)