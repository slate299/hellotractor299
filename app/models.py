from time import timezone
from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tractor(models.Model):
    BRAND_CHOICES = [
        ('new_holland', 'New Holland'),
        ('massey_ferguson', 'Massey Ferguson'),
        ('kijibota', 'Kijibota'),
        ('john_deere', 'John Deere'),
    ]

    LOCATION_CHOICES = [
        ('nyahururu', 'Nyahururu'),
        ('nairobicounty', 'Nairobi County'),
        # Add other locations as necessary
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='tractors')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hours_used = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    images = models.URLField(max_length=500, blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tractors')
    wishlist_users = models.ManyToManyField(User, related_name='wishlist_tractors', blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)  # New field

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name='wishlist_entries')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tractor')
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'

    def __str__(self):
        return f'{self.user.username} - {self.tractor.title}'

class Review(models.Model):
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(
        default=1,
        choices=[(i, str(i)) for i in range(1, 6)],
        help_text="Rating from 1 (lowest) to 5 (highest)"
    )
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tractor Review'
        verbose_name_plural = 'Tractor Reviews'

    def __str__(self):
        return f'Review for {self.tractor.title} by {self.user.username}'


class Implement(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compatibility = models.CharField(max_length=100, default="unknown")
    stock = models.IntegerField()
    images = models.ImageField(upload_to='implements/', blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='implements')
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected
    wishlist_users = models.ManyToManyField(User, related_name='wishlist_implements', blank=True)

    def __str__(self):
        return self.name

