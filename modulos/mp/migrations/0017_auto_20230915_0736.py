# Generated by Django 3.1.3 on 2023-09-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0016_auto_20230915_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mipyme',
            name='num',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
