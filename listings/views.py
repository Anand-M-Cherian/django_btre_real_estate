from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-price').filter(is_published=True)

    # Pagination
    paginator = Paginator(listings, 3)
    page = request.GET.get('page') # page parameter from client request
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        # Get the value from the form field which has the attribute name=keywords
        # <input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)"/>
        keywords = request.GET['keywords']
        # Handling case of empty string by nesting a second if
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices, 
        'bedroom_choices': bedroom_choices, 
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)