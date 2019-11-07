from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20, blank=False)
    brand = models.CharField(max_length=20, blank=False)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.brand}-{self.checked_out}"

    # def __dict__(self):
    #     return {
    #         "name": name,
    #         "brand": brand,
    #         "checked_out": checked_out
    #     }