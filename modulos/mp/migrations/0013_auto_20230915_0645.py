# Generated by Django 3.1.3 on 2023-09-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0012_auto_20230915_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mipyme',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mipyme',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
