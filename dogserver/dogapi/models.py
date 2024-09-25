from django.db import models

# For implementing the 1-5 contstraint on breeds characteristics 
from django.core.validators import MaxValueValidator, MinValueValidator

class Dog(models.Model):
    
    # No contraints on ints for dogs, and this is discrimitary to senior dogs
    #qty = models.IntegerField(
    #        default=1,
    #        validators=[MaxValueValidator(5), MinValueValidator(1)]
    #)
        
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# So how can I capture the error in my view when the validator fails, vs. just the general failure?
class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    friendliness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    def __str__(self):
        return self.name
    
 