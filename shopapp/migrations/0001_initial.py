# Generated by Django 4.0.3 on 2022-06-01 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tazkira', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Initial_asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_asset', models.IntegerField()),
                ('current_asset', models.IntegerField()),
                ('start_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Asset',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('minimum_amount', models.IntegerField()),
                ('current_item_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Roznamcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spender', models.CharField(max_length=30)),
                ('total_spent', models.IntegerField()),
                ('detail', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Store_purchased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_amount', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('purchasing_date', models.DateTimeField()),
                ('item_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('paid', models.DecimalField(decimal_places=5, max_digits=12)),
                ('debit', models.CharField(max_length=10)),
                ('selling_date', models.DateTimeField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.customer', to_field='name')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.store_purchased')),
            ],
        ),
    ]