# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # You can add more fields if needed, e.g. country or founded_year

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    dealer_id = models.IntegerField(default=0)  # Refers to Cloudant dealer ID

    name = models.CharField(max_length=100)

    # Limited choices for type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )

    # Year field with validators
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    # Optional field
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
