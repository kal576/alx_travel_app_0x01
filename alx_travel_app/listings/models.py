from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Listing(models.Model):
    listing_id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    title = models.TextField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    
    def __str__(self):
        return f"{self.guest.username} booking at {self.listing.title}"


class Review(models.Model):
    review_id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    def __str__(self):
        return f"Review by {self.guest.username} for {self.listing.title}"