from rest_framework import serializers
from django.db import transaction
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
    
    def update(self, instance, validated_data):
        instance = Invoice.objects.get(serial_number = instance.serial_number)
        fields = [
                'serial_number', 'status', 'sender_username', 'sender_email', 'sender_country',
                'sender_city', 'sender_street_address', 'sender_postcode', 'reciever_username',
                'reciever_email', 'reciever_country', 'reciever_city', 'reciever_street_address',
                'reciever_postcode', 'payment_terms', 'payment_due_date'
            ]

        for field in fields:
            setattr(instance, field, validated_data[field])
        items_data = validated_data.pop('item_list')
        items = (instance.item_list).all()
        items = list(items)
        instance.sender_username = validated_data.get('name', instance.sender_username)
        for item_data in items_data:
            item = items.pop(0)
            item.name = item_data.get('name', item.name)
            item.price = item_data.get('price', item.price)
            item.quantity = item_data.get('quantity', item.quantity)
            item.save()
        instance.item_total_price = item.total_price
        instance.save()

        return instance