# Generated by Django 5.0.6 on 2024-05-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='serial_number',
            field=models.CharField(default='#UN0128', max_length=15),
        ),
    ]
