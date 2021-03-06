# Generated by Django 3.1.3 on 2020-12-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impressora',
            name='nome',
        ),
        migrations.AddField(
            model_name='impressora',
            name='modelo',
            field=models.CharField(choices=[('1', 'BROTHER DCP6250DW')], default='1', max_length=50, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='impressora',
            name='nivel_toner',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Nível Toner'),
        ),
    ]
