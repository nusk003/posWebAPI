# Generated by Django 2.1.7 on 2019-03-30 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('debit', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accounts', to='Supplier.Supplier')),
            ],
        ),
    ]
