from rest_framework import serializers
from django.db import transaction
from .models import Invoice, Item






class ItemSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    class Meta:
        model = Item
        fields = ['id','name', 'price', 'quantity', 'total_price']


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
        new_items = validated_data.pop('item_list')
        old_items = instance.item_list.values()
        
        instance = super(InvoiceSerializer, self).update(instance, validated_data)
        for item in old_items:
            Item.objects.get(id=item["id"]).delete()
        instance.item_list.set([])
        instance.item_total_price = 0
        for item in new_items:
            item_obj = Item.objects.create(**item)
            instance.item_total_price += item_obj.total_price
            instance.item_list.add(item_obj)
        instance.save()
        return instance