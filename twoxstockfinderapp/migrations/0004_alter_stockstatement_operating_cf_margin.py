# Generated by Django 5.1.6 on 2025-02-10 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twoxstockfinderapp', '0003_alter_stockstatement_bps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockstatement',
            name='operating_cf_margin',
            field=models.FloatField(blank=True, default=4.43, null=True, verbose_name='営業CFマージン'),
        ),
    ]
