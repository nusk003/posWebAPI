# Generated by Django 2.1.7 on 2019-03-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinvoice',
            name='customer',
        ),
    ]