# Generated by Django 5.0.6 on 2024-05-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='serial_number',
            field=models.CharField(default=2, max_length=7),
            preserve_default=False,
        ),
    ]