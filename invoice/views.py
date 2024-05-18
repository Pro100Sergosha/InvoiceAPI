from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Item, Invoice
from .serializers import ItemSerializer, InvoiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class InvoiceViewset(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    

class ChangeInvoiceStatus(APIView):
    def get(self, request, id, new_status):

        try:
            invoice = Invoice.objects.get(id=id)
        except Invoice.DoesNotExist:
            return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if new_status not in ['paid', 'pending', 'draft']:
            return Response({'message': 'There is no such status(Write: mark_as_ paid/draft/pending)'}, status= status.HTTP_400_BAD_REQUEST)
        else:
            invoice.status = new_status
            invoice.save()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

