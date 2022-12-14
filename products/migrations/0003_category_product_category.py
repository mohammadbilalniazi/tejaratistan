# Generated by Django 4.1.1 on 2022-09-23 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_purchased_price_product_selling_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='products.category'),
        ),
    ]
