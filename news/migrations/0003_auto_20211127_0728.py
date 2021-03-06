# Generated by Django 3.1.13 on 2021-11-27 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211126_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1111111111, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news_img/'),
        ),
    ]
