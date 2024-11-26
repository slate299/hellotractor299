from django.contrib import admin
from .models import Tractor, Brand, Wishlist, Review, Implement

# Register the Tractor model
class TractorAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'location', 'hours_used', 'age', 'seller')
    search_fields = ('title', 'brand__name', 'location')
    list_filter = ('brand', 'seller')
    list_editable = ('price', 'hours_used', 'age')  # Example fields you might want to edit directly

admin.site.register(Tractor, TractorAdmin)

# Register the Brand model
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display only the brand name
    search_fields = ('name',)  # Enable searching by brand name

admin.site.register(Brand, BrandAdmin)

# Register the Wishlist model
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'tractor', 'added_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'tractor__title')

admin.site.register(Wishlist, WishlistAdmin)

# Register the Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('tractor', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('tractor__title', 'user__username')

admin.site.register(Review, ReviewAdmin)

class ImplementAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', "compatibility", "stock", 'seller')  # Ensure category is present here
    search_fields = ('name', 'category', 'compatibility')  # If category is a foreign key, reference it correctly
    list_filter = ('category', 'seller')
    list_editable = ('price', 'stock')# Include category filter if necessary

admin.site.register(Implement, ImplementAdmin)
