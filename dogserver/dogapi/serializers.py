from rest_framework import serializers

# Dog and Breed models
from .models import Dog
from .models import Breed

# Modified Dog serializer for the new dog details
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']

# New Breed serializer
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount' , 'exerciseneeds']

