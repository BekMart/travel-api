from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer


class LocationList(generics.ListAPIView):
    """
    List all locations
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveAPIView):
    """
    Retrieve a location by slug
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'slug'
