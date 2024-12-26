from rest_framework import serializers
from listings.models import Listing
from contacts.models import Contact

class GetListingsSerializer(serializers.ModelSerializer):
    list_date = serializers.ReadOnlyField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'is_published', 'realtor', 'list_date']

class CreateListingsSerializer(serializers.ModelSerializer):
    list_date = serializers.ReadOnlyField()

    class Meta:
        model = Listing
        fields = '__all__'