from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from location.models import Location
from location.serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
