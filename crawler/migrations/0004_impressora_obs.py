# Generated by Django 3.1.3 on 2020-12-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_auto_20201201_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='impressora',
            name='obs',
            field=models.CharField(blank=True, max_length=50, verbose_name='Obs'),
        ),
    ]