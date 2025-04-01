from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer


class LocationList(generics.ListAPIView):
    """
    List all locations
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
