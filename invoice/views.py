from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Item, Invoice
from .serializers import ItemSerializer, InvoiceSerializer




class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class InvoiceViewset(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
