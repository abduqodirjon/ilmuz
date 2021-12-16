# Generated by Django 3.1.13 on 2021-11-27 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20211127_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Kategoriyasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=250, verbose_name='Mazmuni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_img', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_full',
            field=models.TextField(verbose_name="To'liq matni"),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Sarlavha'),
        ),
    ]