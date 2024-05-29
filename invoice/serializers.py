from rest_framework import serializers
from .models import Invoice, Item
from drf_writable_nested import WritableNestedModelSerializer





class ItemSerializer(WritableNestedModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    class Meta:
        model = Item
        fields = ['id','name', 'price', 'quantity', 'total_price']


class InvoiceSerializer(WritableNestedModelSerializer):
    item_list = ItemSerializer(many = True)
    item_total_price = serializers.FloatField(read_only = True)
    serial_number = serializers.CharField(read_only = True)
    payment_end_date = serializers.DateField(read_only = True)
    class Meta:
        model = Invoice
        fields = '__all__'