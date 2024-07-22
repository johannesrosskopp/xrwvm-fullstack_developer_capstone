from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=200)

    def __str__(self):
        return "{} from {}".format(self.name, self.country_of_origin)



class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan'),
        ('PICKUP', 'Pickup'),
        ('HATCHBACK', 'Hatchback'),
        ('SPORTS_CAR', 'Sports Car'),
        ('DIESEL', 'Diesel'),
        ('HYBRID', 'Hybrid'),
        ('ELECTRIC', 'Electric'),
    ]

    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    seats = models.IntegerField(default=5,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ])
    

    def __str__(self):
        return self.name  # Return the name as the string representation
