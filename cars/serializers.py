from .models import Car, Rent
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'checked_out', 'rentee']


class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = ['id', 'name', 'brand', 'rentee']
