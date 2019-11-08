# from django.shortcuts import render
from .serializers import CarSerializer, RentSerializer
from .models import Car, Rent
from rest_framework import viewsets
from django.http import JsonResponse
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cars to be viewed or edited.
    """
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer

class RentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to rent a car.
    """
    queryset = Rent.objects.all().order_by('id')
    serializer_class = RentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        name = data.get("name")
        brand = data.get("brand")
        rentee = data.get("rentee")

        available_cars = Car.objects.filter(name=name, brand=brand, checked_out=False)

        # If filter returns no available cars by name and brand:
        if not available_cars:
            available_brand_cars = Car.objects.filter(brand=brand, checked_out=False)

            # If no other cars are available for the brand"
            if not available_brand_cars:
                available_brands = list(Car.objects.values_list('brand', flat=True))
                if brand in available_brands:
                    available_brands.remove(brand)
                
                return JsonResponse({"message": f"Car is not available. No other cars for brand {brand} are available either. Please try another brand. [{', '.join(available_brands)}]"})

            # Get avaiable car names for brand
            car_names_for_brand = available_brand_cars.values_list('name', flat=True)
            return JsonResponse({"message": f"Car is not available; here are alternatives from the same brand: | {', '.join(car_names_for_brand)} |"})

        selected = available_cars.first()
        selected.rentee = rentee
        selected.checked_out = True
        selected.save()
        

        return JsonResponse({"message": f"Car found {selected}"})