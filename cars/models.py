from django.db import models

# Create your models here.
class Car(models.Model):
    """Car model."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    checked_out = models.BooleanField(default=False)
    rentee = models.CharField(max_length=30, blank=True)
    """
    Add additional column (year) here:

    The column we want to add it a column for the year-model of the car.

    For example:
    - Mercedes have models such as E280, or S63 AMG. 
    However those models can be created over the years; meaning there will be a 1997 E280 
    and there could be a 2000 E280 as the next generation of cars are created in the 
    year 2000 (the next production period for E280's.)

    So this additional column is for the year the car was made

    NOTE: Make sure to add the field to the CarSerializer as well as the 
    Rent model below and it's appropriate serializer (RentSerializer)
    """

    def __str__(self):
        return f"{self.name}_{self.brand}_{self.checked_out}"


class Rent(models.Model):
    """Rent a car model."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    rentee = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return f"{self.name}_{self.brand}_{self.checked_out}"