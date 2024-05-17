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
    
    def update(self, instance, validated_data):
        invoice = Invoice.objects.get(serial_number = instance.serial_number)
        invoice.serial_number = validated_data['serial_number']
        invoice.status = validated_data['status']
        invoice.sender_username = validated_data['sender_username']
        invoice.sender_email = validated_data['sender_email']
        invoice.sender_country = validated_data['sender_country']
        invoice.sender_city = validated_data['sender_city']
        invoice.sender_street_address = validated_data['sender_street_address']
        invoice.sender_postcode = validated_data['sender_postcode']
        invoice.reciever_username = validated_data['reciever_username']
        invoice.reciever_email = validated_data['reciever_email']
        invoice.reciever_country = validated_data['reciever_country']
        invoice.reciever_city = validated_data['reciever_city']
        invoice.reciever_street_address = validated_data['reciever_street_address']
        invoice.reciever_postcode = validated_data['reciever_postcode']
        invoice.payment_terms = validated_data['payment_terms']
        invoice.payment_due_date = validated_data['payment_due_date']
        items_data = validated_data.pop('item_list')
        for item_list in items_data:
            item = Item.objects.update(**item_list)
            invoice.item_total_price += item.total_price
            invoice.item_list.add(item)
        invoice.save()
        return invoice