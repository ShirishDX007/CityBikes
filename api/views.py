from rest_framework import generics 
from listings.models import Listings
from rest_framework.views import APIView
from .serializers import ListingSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.

class ListingList(generics.ListCreateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer

@api_view(['POST', 'GET'])
def send_mail_for_New_listing(request):
    serializer = ListingSerializer(data=request.data)
    if serializer.is_valid():
        new_listing = serializer.save()
        subject = "New Listing is created"
        message = render_to_string('emails/listing_created_email.txt', {'listing': instance})
        html_message = render_to_string('emails/listing_created_email.html', {'listing': instance})
        recipients_list = [instance.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients_list, html_message=html_message, fail_silently=False)

        return Response({'message': 'Email sent successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
