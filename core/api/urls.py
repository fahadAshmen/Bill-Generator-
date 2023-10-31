from django.urls import path
from invoice_mgmt.views import BillAPIView, BillAPI

urlpatterns = [
    path('',BillAPI.as_view(),name='bills'),
    path('create-bills/',BillAPIView.as_view(),name='create-bills'),
]
