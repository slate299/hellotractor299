from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Tractor
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = "Upload tractor images to Tractor models from provided URLs"

    def handle(self, *args, **kwargs):
        csv_path = r'C:\Users\NATASHA\Desktop\Asset_models_urls.csv'

        try:
            data = pd.read_csv(csv_path)
            data.columns = data.columns.str.strip()
            data['model'] = data['model'].str.strip()

            for index, row in data.iterrows():
                model_name = row['model']
                image_url = row['tractor_model_logo_url']

                if pd.isnull(image_url):
                    self.stdout.write(self.style.WARNING(f"Skipping {model_name}: No image URL provided"))
                    continue

                self.stdout.write(self.style.SUCCESS(f"Processing {model_name}: {image_url}"))

                tractor = Tractor.objects.filter(title__iexact=model_name).first()

                if not tractor:
                    self.stdout.write(self.style.ERROR(f"Tractor model not found in database: {model_name}"))
                    continue

                try:
                    response = requests.get(image_url)
                    response.raise_for_status()

                    tractor_image = ContentFile(response.content)
                    tractor.images.save(f"{model_name.replace(' ', '_').lower()}_image.jpg", tractor_image, save=True)

                    self.stdout.write(self.style.SUCCESS(f"Successfully updated {model_name} with the image"))

                except requests.RequestException as e:
                    self.stdout.write(self.style.ERROR(f"Error downloading image for {model_name}: {e}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing {model_name}: {e}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"CSV file not found at: {csv_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error reading the CSV file: {e}"))
