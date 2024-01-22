from rest_framework import serializers
from listings.models import Listings

class ListingSerializer(serializers.ModelSerializer):
    listings = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listings
        fields = '__all__'

