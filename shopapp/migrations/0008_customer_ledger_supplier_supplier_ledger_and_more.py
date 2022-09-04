# Generated by Django 4.0.3 on 2022-09-02 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopapp', '0007_alter_purchase_detail_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('narration', models.CharField(max_length=80)),
                ('transation_date', models.CharField(max_length=80)),
                ('creator_kahatha', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tazkira', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Supplier_Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('narration', models.CharField(max_length=80)),
                ('transation_date', models.CharField(max_length=80)),
                ('creator_kahatha', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.supplier')),
            ],
        ),
        migrations.RenameModel(
            old_name='Initial_asset',
            new_name='Asset',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name_plural': 'Log'},
        ),
        migrations.DeleteModel(
            name='Customer_kahatha_received',
        ),
        migrations.AddField(
            model_name='customer_ledger',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.customer'),
        ),
    ]
