# Generated by Django 3.1.3 on 2023-07-21 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0002_mipyme_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='mipyme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='mp.mipyme'),
        ),
    ]