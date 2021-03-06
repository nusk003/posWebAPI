# Generated by Django 2.1.7 on 2019-03-30 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sales', '0001_initial'),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deliveryCharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField()),
                ('isCancel', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='Employee.User')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='Sales.CustomerInvoice')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxDistance', models.IntegerField()),
                ('minDistance', models.IntegerField()),
                ('charge', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleNo', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleType', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicleType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.VehicleType'),
        ),
        migrations.AddField(
            model_name='deliverycharge',
            name='vehicleType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.VehicleType'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='Transport.Vehicle'),
        ),
    ]
