from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tractor-listings/', views.tractor_listings, name='tractor-listings'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:tractor_id>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('remove-from-wishlist/<int:tractor_id>/', views.remove_from_wishlist, name='remove-from-wishlist'),
    path('tractor-details/<int:tractor_id>/', views.tractor_details, name='tractor-details'),
    path('add-review/<int:tractor_id>/', views.add_review, name='add-review'),
    path('create-tractor-listing/', views.create_tractor_listing, name='create-tractor-listing'),  # New path for tractor listing creation
    path('create-implement-listing/', views.create_implement_listing, name='create-implement-listing'),  # New path for implement listing creation
    path('delete-listing/<int:tractor_id>/', views.delete_listing, name='delete-listing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('my-listings/', views.seller_listings, name='seller-listings'),
    path('edit-listing/<int:tractor_id>/', views.edit_listing, name='edit-listing'),
    path('implements/', views.implement_list, name='implement-listings'),
    path('implement/<int:implement_id>/', views.implement_details, name='implement-details'),
]
