# Generated by Django 3.1.3 on 2020-12-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20201201_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impressora',
            name='status',
            field=models.CharField(choices=[('0', 'OFFLINE'), ('1', 'ONLINE')], max_length=50, verbose_name='Status'),
        ),
    ]