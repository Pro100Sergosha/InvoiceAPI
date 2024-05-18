# Generated by Django 5.0.6 on 2024-05-18 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_alter_invoice_reciever_email_alter_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='item_list',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='serial_number',
            field=models.CharField(default='#AI6316', max_length=15),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_list',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='invoice.item'),
            preserve_default=False,
        ),
    ]