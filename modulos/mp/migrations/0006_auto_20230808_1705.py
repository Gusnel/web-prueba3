# Generated by Django 3.1.3 on 2023-08-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0005_auto_20230808_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='img'),
        ),
    ]
