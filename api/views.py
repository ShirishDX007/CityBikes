from rest_framework import generics 
from listings.models import Listings
from .serializers import ListingSerializer


# Create your views here.

class ListingList(generics.ListCreateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer
