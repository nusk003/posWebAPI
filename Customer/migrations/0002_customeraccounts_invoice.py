# Generated by Django 2.1.7 on 2019-03-30 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0002_remove_customerinvoice_customer'),
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccounts',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales.CustomerInvoice'),
        ),
    ]
