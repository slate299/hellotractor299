from django import forms
from .models import Tractor, Wishlist, Review, Brand, Implement
from .helpers import upload_to_drive

# Tractor Form
class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractor
        fields = ['title', 'description', 'brand', 'price', 'hours_used', 'age', 'location', 'images', 'seller']

    def clean_images(self):
        image_file = self.cleaned_data.get('images')

        if image_file:
            # Save the file to Google Drive and get the URL
            file_name = image_file.name
            drive_url = upload_to_drive(image_file.temporary_file_path(), file_name)
            return drive_url  # Save the URL in the database instead of the file itself

        return image_file


# Implement Form
class ImplementForm(forms.ModelForm):
    class Meta:
        model = Implement
        fields = ['name', 'category', 'price', 'compatibility', 'stock', 'images', 'seller']

    def clean_images(self):
        image_file = self.cleaned_data.get('images')

        if image_file:
            # Save the file to Google Drive and get the URL
            file_name = image_file.name
            drive_url = upload_to_drive(image_file.temporary_file_path(), file_name)
            return drive_url  # Save the URL in the database instead of the file itself

        return image_file


# Wishlist Form
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['tractor']


# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']


# Tractor Listing Form with Custom Validation
class TractorListingForm(forms.ModelForm):
    class Meta:
        model = Tractor
        fields = ['title', 'description', 'brand', 'price', 'hours_used', 'location', 'age', 'images']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return price

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError('Location cannot be empty')
        return location

    def clean_images(self):
        image_file = self.cleaned_data.get('images')

        if image_file:
            # Save the file to Google Drive and get the URL
            file_name = image_file.name
            drive_url = upload_to_drive(image_file.temporary_file_path(), file_name)
            return drive_url  # Save the URL in the database instead of the file itself

        return image_file
