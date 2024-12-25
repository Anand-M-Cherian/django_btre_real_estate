from rest_framework import serializers
from listings.models import Listing

class GetListingsSerializer(serializers.ModelSerializer):
    list_date = serializers.ReadOnlyField()

    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['id', 'title', 'realtor', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'list_date', ]