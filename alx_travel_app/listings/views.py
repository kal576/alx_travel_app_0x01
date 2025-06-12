from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ViewSet):
    """Listing viewset to perform CRUD operations"""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ViewSet):
    """Listing viewset to perform CRUD operations"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer