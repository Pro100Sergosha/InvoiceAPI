from rest_framework import serializers
from .models import Invoice, Item




class ItemSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    class Meta:
        model = Item
        fields = ['name', 'price', 'quantity', 'total_price']


class InvoiceSerializer(serializers.ModelSerializer):
    item_list = ItemSerializer(many = True)
    item_total_price = serializers.FloatField(read_only = True)
    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('item_list')
        invoice = Invoice.objects.create(**validated_data)
        for item_list in items_data:
            item = Item.objects.create(**item_list)
            invoice.item_total_price += item.total_price
            invoice.item_list.add(item)
        invoice.save()
        return invoice