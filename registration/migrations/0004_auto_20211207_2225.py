# Generated by Django 3.1.13 on 2021-12-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20211207_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_img', verbose_name='Rasm:'),
        ),
    ]
