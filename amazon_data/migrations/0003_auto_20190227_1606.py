# Generated by Django 2.1.3 on 2019-02-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_data', '0002_auto_20190227_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band_sell',
            name='month',
            field=models.IntegerField(verbose_name='月份'),
        ),
        migrations.AlterField(
            model_name='band_sell',
            name='weeks',
            field=models.IntegerField(verbose_name='周数'),
        ),
    ]