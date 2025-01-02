from rest_framework import serializers
from listings.models import Listing
from contacts.models import Contact

class ListingsSerializer(serializers.ModelSerializer):
    list_date = serializers.ReadOnlyField()

    class Meta:
        model = Listing
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    list_date = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = '__all__'