from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator
import datetime
import random
import string

def serial_number_generator():
    return  '#' + ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k= 4))
    
class Item(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField(null=True, blank=True)


class Invoice(models.Model):
    serial_number = models.CharField(max_length=15, default=serial_number_generator())
    PAYMENT_CHOICES = (
        (1, '1 Day'),
        (2, '7 Days'),
        (3, '14 Days'),
        (4, '30 Days'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('draft', 'Draft'), 
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=7, default='draft')

    item_list = models.ManyToManyField(Item)

    sender_username = models.CharField(max_length=50)
    sender_email = models.EmailField(unique=True)
    sender_country = models.CharField(max_length=50)
    sender_city = models.CharField(max_length=50)
    sender_street_address = models.CharField(max_length=50)
    sender_postcode = models.CharField(max_length=30)

    reciever_username = models.CharField(max_length=50)
    reciever_email = models.EmailField()
    reciever_country = models.CharField(max_length=50)
    reciever_city = models.CharField(max_length=50)
    reciever_street_address = models.CharField(max_length=50)
    reciever_postcode = models.CharField(max_length=30)
    
    payment_terms = models.IntegerField(choices=PAYMENT_CHOICES)
    payment_due_date = models.DateField(blank=True, null=True)
    item_total_price = models.FloatField(default=0, blank=True, null=True)
    description = models.TextField()


    def __str__(self):
        return f'Sender Informaiton: {self.sender_username}, {self.sender_email}, {self.sender_city}, {self.sender_country}, {self.sender_street_address}, {self.sender_postcode}.\n \
                Receivier Information: {self.reciever_username}, {self.reciever_email}, {self.reciever_city}, {self.reciever_country}, {self.reciever_street_address}, {self.reciever_postcode}'
                


@receiver(pre_save, sender=Invoice)
def set_payment_due_date(sender, instance, **kwargs):
    if instance.payment_terms:
        if instance.payment_terms == 1:
            payment_period = datetime.timedelta(days=1)
        elif instance.payment_terms == 2:
            payment_period = datetime.timedelta(days=7)
        elif instance.payment_terms == 3:
            payment_period = datetime.timedelta(days=14)
        elif instance.payment_terms == 4:
            payment_period = datetime.timedelta(days=30)

        instance.payment_due_date = datetime.date.today() + payment_period

@receiver(pre_save, sender=Item)
def set_payment_due_date(sender, instance, **kwargs):
    if instance.price and instance.quantity:
        instance.total_price = instance.price * instance.quantity

