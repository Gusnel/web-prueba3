# Generated by Django 3.1.3 on 2023-09-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0010_auto_20230915_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mipyme',
            old_name='productos',
            new_name='ubicacion',
        ),
    ]
