from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_locations = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Naivasha"]
        titles = ["Cozy Apartment", "Beachfront Villa", "Modern Studio", "Luxury Suite", "Budget Room"]

        for i in range[10]:
            Listing.objects.create(
                title=random.choice(titles),
                description="This is a lovely place to stay.",
                price_per_night=random.randint(1500, 10000),
                location=random.choice(sample_locations),
                available=True
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully seeded 10 listings."))