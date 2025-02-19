# Generated by Django 5.1.6 on 2025-02-10 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twoxstockfinderapp', '0002_alter_stockstatement_bps_alter_stockstatement_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockstatement',
            name='bps',
            field=models.FloatField(blank=True, default=592.01, null=True, verbose_name='BPS (1株あたり純資産)'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='company_name',
            field=models.CharField(blank=True, default='三菱ロジスネクスト', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='dividend_payout_ratio',
            field=models.FloatField(blank=True, default=118.9, null=True, verbose_name='配当性向'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='financing_cf',
            field=models.IntegerField(blank=True, default=-4601000000, null=True, verbose_name='財務キャッシュフロー'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='investing_cf',
            field=models.IntegerField(blank=True, default=-19243000000, null=True, verbose_name='投資キャッシュフロー'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='long_term_loans',
            field=models.IntegerField(blank=True, default=131678000000, null=True, verbose_name='長期借入金'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='registered_date',
            field=models.DateField(default=datetime.date(2025, 2, 10)),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='revenue',
            field=models.IntegerField(blank=True, default=465406000000, null=True, verbose_name='売上高'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='roe',
            field=models.FloatField(blank=True, default=1.14, null=True, verbose_name='ROE (自己資本利益率)'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='shareholders_equity',
            field=models.FloatField(blank=True, null=True, verbose_name='株主資本'),
        ),
        migrations.AlterField(
            model_name='stockstatement',
            name='year',
            field=models.IntegerField(default=2022, verbose_name='年度'),
        ),
    ]
