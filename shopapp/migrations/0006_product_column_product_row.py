# Generated by Django 4.0.5 on 2022-08-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_rename_item_name_purchase_detail_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='column',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='row',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
