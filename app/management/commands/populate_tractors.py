from django.core.management.base import BaseCommand
from app.models import Tractor, Brand
import random

class Command(BaseCommand):
    help = "Populate the database with pseudo tractor listings"

    def handle(self, *args, **kwargs):
        tractors = []
        brand_names = ["John Deere", "Massey Ferguson", "New Holland", "Kubota", "Sonalika"]
        locations = ["Nairobi", "Mombasa", "Kisumu", "Nyeri", "Nakuru"]
        titles = ["Model A", "Model B", "Model C", "Model D", "Model E"]

        # Ensure all brands exist in the Brand model
        brands = {name: Brand.objects.get_or_create(name=name)[0] for name in brand_names}

        for i in range(236):
            title = f"{random.choice(brand_names)} {random.choice(titles)}"
            brand_name = random.choice(brand_names)
            brand = brands[brand_name]  # Fetch the corresponding Brand instance
            location = random.choice(locations)
            price = random.randint(500000, 3000000)  # Price range in KES
            hours_used = random.randint(100, 5000)  # Random usage hours

            tractors.append(Tractor(
                title=title,
                brand=brand,  # Assign the Brand instance
                location=location,
                price=price,
                hours_used=hours_used,
                description="This is a pseudo description for a tractor listing.",
                age=random.randint(1, 10)  # Age in years
            ))

        Tractor.objects.bulk_create(tractors)
        self.stdout.write(self.style.SUCCESS(f"Successfully added 236 pseudo tractor listings"))
