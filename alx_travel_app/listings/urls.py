from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

router = DefaultRouter()

urlpatterns = [
    path('api/listings', ListingViewSet),
    path('api/bookings', BookingViewSet)
    ]