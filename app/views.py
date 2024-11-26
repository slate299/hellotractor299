from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Tractor, Wishlist, Review, Brand, Implement
from .forms import WishlistForm, ReviewForm, TractorForm, ImplementForm
from django.core.paginator import Paginator

def index(request):
    tractors = Tractor.objects.all()[:3]
    implements = Implement.objects.all()[:3]  # Get the top 3 implements
    return render(request, 'index.html', {'tractors': tractors, 'implements': implements})


def filter_tractors(request, tractors):
    # Get filter criteria from GET parameters
    brand = request.GET.get('brand')
    location = request.GET.get('location')
    search = request.GET.get('search')

    # Apply filters if criteria are present
    if brand:
        tractors = tractors.filter(brand__name=brand)
    if location:
        tractors = tractors.filter(location__icontains=location)
    if search:
        tractors = tractors.filter(title__icontains=search)

    return tractors


def tractor_listings(request):
    tractors = Tractor.objects.all()  # Get all tractors initially
    paginator = Paginator(tractors, 20)
    tractors = filter_tractors(request, tractors)  # Apply filters based on user input

    # Get unique brands and locations dynamically
    brands = Tractor.objects.values_list('brand__name', flat=True).distinct()
    locations = Tractor.objects.values_list('location', flat=True).distinct()

    # Capture the filter values to persist the selections
    selected_brand = request.GET.get('brand')
    selected_location = request.GET.get('location')
    search_query = request.GET.get('search')

    context = {
        'tractors': tractors,
        'brands': brands,
        'locations': locations,
        'selected_brand': selected_brand,
        'selected_location': selected_location,
        'search_query': search_query,
    }
    return render(request, 'tractor-listings.html', context)


@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, tractor=tractor)
    if created:
        messages.success(request, "Tractor added to wishlist!")
    else:
        messages.info(request, "Tractor already in your wishlist.")
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, tractor=tractor).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, "Tractor removed from your wishlist!")
    else:
        messages.warning(request, "This tractor is not in your wishlist.")

    return redirect('wishlist')


@login_required
def create_tractor_listing(request):
    if request.method == 'POST':
        tractor_form = TractorForm(request.POST, request.FILES)
        if tractor_form.is_valid():
            tractor = tractor_form.save(commit=False)
            tractor.seller = request.user  # Assign the logged-in user as the seller
            tractor.save()
            messages.success(request, "Tractor listing created successfully!")
        else:
            print(tractor_form.errors)  # Print form errors to debug why it's not saving
            messages.error(request, "There was an error with your submission.")
    else:
        tractor_form = TractorForm()
    return render(request, 'create-tractor-listing.html', {'tractor_form': tractor_form})


@login_required
def create_implement_listing(request):
    if request.method == 'POST':
        implement_form = ImplementForm(request.POST, request.FILES)
        if implement_form.is_valid():
            implement = implement_form.save(commit=False)
            implement.seller = request.user  # Assign the logged-in user as the seller
            implement.save()
            messages.success(request, "Implement listing created successfully!")
        else:
            print(implement_form.errors)  # Print form errors to debug why it's not saving
            messages.error(request, "There was an error with your submission.")
    else:
        implement_form = ImplementForm()
    return render(request, 'create-implement-listing.html', {'implement_form': implement_form})


@login_required
def delete_listing(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id, seller=request.user)
    tractor.delete()
    messages.success(request, "Listing deleted successfully.")
    return redirect('tractor-listings')


def tractor_details(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    reviews = tractor.reviews.all()
    is_in_wishlist = Wishlist.objects.filter(user=request.user,
                                             tractor=tractor).exists() if request.user.is_authenticated else False
    return render(request, 'tractor-details.html', {
        'tractor': tractor,
        'reviews': reviews,
        'is_in_wishlist': is_in_wishlist,
    })


def implement_details(request, implement_id):
    implement = Implement.objects.get(id=implement_id)
    return render(request, 'implement-details.html', {'implement': implement})


def implement_list(request):
    implements = Implement.objects.all()

    # Get unique categories dynamically
    categories = Implement.objects.values_list('category', flat=True).distinct()

    # Filter by category
    category = request.GET.get('category')
    if category:
        implements = implements.filter(category=category)

    # Search by name
    search = request.GET.get('search')
    if search:
        implements = implements.filter(name__icontains=search)

    context = {
        'implements': implements,
        'categories': categories,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'implement-listings.html', context)


@login_required
def add_review(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tractor = tractor
            review.user = request.user
            review.save()
            messages.success(request, "Review added successfully.")
            return redirect('tractor-details', tractor_id=tractor.id)
    else:
        form = ReviewForm()
    return render(request, 'add-review.html', {'form': form, 'tractor': tractor})


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Logged out successfully.")
        return super().dispatch(request, *args, **kwargs)


@login_required
def seller_listings(request):
    tractors = Tractor.objects.filter(seller=request.user)
    return render(request, 'seller-listings.html', {'tractors': tractors})


@login_required
def edit_listing(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id, seller=request.user)
    if request.method == 'POST':
        form = TractorForm(request.POST, request.FILES, instance=tractor)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing updated successfully.")
            return redirect('seller-listings')
    else:
        form = TractorForm(instance=tractor)
    return render(request, 'edit-listing.html', {'form': form, 'tractor': tractor})
