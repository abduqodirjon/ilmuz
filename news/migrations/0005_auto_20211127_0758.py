# Generated by Django 3.1.13 on 2021-11-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211127_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news_img//%Y/%m/%d'),
        ),
    ]