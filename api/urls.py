from django.urls import path
from .views import ListingList, ListingDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('ListingList/', ListingList.as_view(), name='listing_list'),
    path('ListingDetail/<int:pk>/', ListingDetail.as_view(), name='listing_detail'),
    #jwt urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]