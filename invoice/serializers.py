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
                'status', 'sender_username', 'sender_email', 'sender_country',
                'sender_city', 'sender_street_address', 'sender_postcode', 'reciever_username',
                'reciever_email', 'reciever_country', 'reciever_city', 'reciever_street_address',
                'reciever_postcode', 'payment_terms', 'payment_start_date',
            ]

        for field in fields:
            setattr(instance, field, validated_data[field])
        items_data = validated_data.copy()
        items_data = items_data.pop('item_list')
        items = (instance.item_list).all()
        items = list(items)
        instance.sender_username = validated_data.get('name', instance.sender_username)
        new_items_data = items_data.copy()
        new_items_list = []
        count = len(items)
        for item_data in items_data:
            if not count == 0:
                count-=1
                item = items.pop(0)
                item.name = item_data.get('name', item.name)
                item.price = item_data.get('price', item.price)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            elif count == 0:
                if not items and new_items_data:
                    new_item = Item.objects.create(
                        name = new_items_data[0]['name'],
                        price = new_items_data[0]['price'],
                        quantity = new_items_data[0]['quantity'],
                        total_price = new_items_data[0]['quantity'] * new_items_data[0]['price']
                        )
                    new_items_list.append(new_item)
                    new_items_data.pop()
                

        [instance.item_list.add(item) for item in new_items_list]
        instance.item_total_price = 0
        count = len(validated_data['item_list'])
        for i in validated_data['item_list']:
            if count == 0:
                break
            else:
                total_price = i['price'] * i['quantity']
                instance.item_total_price += total_price
        instance.save()

        return instance