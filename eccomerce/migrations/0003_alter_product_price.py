# Generated by Django 4.1.7 on 2023-03-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccomerce', '0002_rename_oderdetail_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
