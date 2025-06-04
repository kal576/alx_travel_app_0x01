from rest_framework import serializers
from .models import Listing, Booking

#serializer for the Listings model
class ListingSerializer(serializers.ModelSerializer):
    """
    Returns all the fields inside Booking in json format
    """
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """
    Returns all the fields inside Booking in json format
    """
    class Meta:
        model = Booking
        fields = '__all__'
