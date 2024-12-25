from rest_framework import generics
from .serializers import GetListingsSerializer
from listings.models import Listing

# Create your views here.

class GetListings(generics.ListAPIView):
    serializer_class = GetListingsSerializer

    def get_queryset(self):
        listings = Listing.objects.order_by('-list_date')
        return listings
