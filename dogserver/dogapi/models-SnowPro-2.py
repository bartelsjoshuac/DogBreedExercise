from django.db import models

# For implementing the 1-5 contstraint on breeds characteristics 
from django.core.validators import MaxValueValidator, MinValueValidator

# Something to contrain the possible breed sizes
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Dog(models.Model):
        
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Breed(models.Model):
    name = models.CharField(max_length=100)
    SIZE_CHOICES = ( 
    ('Tiny', 'Tiny'), 
    ('Small', 'Small'), 
    ('Medium', 'Medium'), 
    ('Large', 'Large'),
    ) 

    size = models.CharField(max_length=6, sizes=SIZE_CHOICES)
        
    # Int values 1-5 only, and this is working
    # So how can I capture the error in my view when the validator fails, vs. just the general failure?
    friendliness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])




 