# webhook_handler/urls.py

from django.urls import path
from .views import AccountListCreateView, AccountDetailView, DestinationListCreateView, DestinationDetailView

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('destinations/', DestinationListCreateView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
]
