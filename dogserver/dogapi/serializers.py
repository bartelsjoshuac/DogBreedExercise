from rest_framework import serializers
from .models import Dog
from .models import Breed

#Modified Dog serializer for the new options
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']


# My Breed serializer
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount' , 'exerciseneeds']


