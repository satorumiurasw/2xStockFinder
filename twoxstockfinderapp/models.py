from django.db import models
from datetime import date

# Create your models here.
class StockStatement(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField('銘柄コード', default=7105)  # 銘柄コード
    year = models.IntegerField('年度', default=2025)  # 年度
    total_assets = models.IntegerField('総資産', blank=True, null=True)  # 総資産
    net_assets = models.IntegerField('純資産', blank=True, null=True)  # 純資産
    shareholders_equity = models.FloatField('株主資本', blank=True, null=True)  # 株主資本
    retained_earnings = models.IntegerField('利益剰余金', blank=True, null=True)  # 利益剰余金
    short_term_loans = models.IntegerField('短期借入金', blank=True, null=True)  # 短期借入金
    long_term_loans = models.IntegerField('長期借入金', default=131678000000)  # 長期借入金
    bps = models.FloatField('BPS (1株あたり純資産)', default=592.01)  # BPS (1株あたり純資産)
    equity_ratio = models.FloatField('自己資本比率', blank=True, null=True)  # 自己資本比率
    operating_cf = models.IntegerField('営業キャッシュフロー', blank=True, null=True)  # 営業キャッシュフロー
    investing_cf = models.IntegerField('投資キャッシュフロー', default=-19243000000)  # 投資キャッシュフロー
    financing_cf = models.IntegerField('財務キャッシュフロー', default=-4601000000)  # 財務キャッシュフロー
    capital_expenditure = models.IntegerField('設備投資', blank=True, null=True)  # 設備投資
    cash_equivalents = models.IntegerField('現金同等物', blank=True, null=True)  # 現金同等物
    operating_cf_margin = models.FloatField('営業CFマージン', default=4.43)  # 営業CFマージン
    revenue = models.IntegerField('売上高', default=465406000000)  # 売上高
    operating_income = models.IntegerField('営業利益', blank=True, null=True)  # 営業利益
    ordinary_income = models.IntegerField('経常利益', blank=True, null=True)  # 経常利益
    net_income = models.IntegerField('純利益', blank=True, null=True)  # 純利益
    eps = models.FloatField('EPS (1株当たり利益)', blank=True, null=True)  # EPS (1株当たり利益)
    roe = models.FloatField('ROE (自己資本利益率)', default=1.14)  # ROE (自己資本利益率)
    roa = models.FloatField('ROA (総資産利益率)', blank=True, null=True)  # ROA (総資産利益率)
    dividend_per_share = models.IntegerField('一株配当', blank=True, null=True)  # 一株配当
    retained_earnings_dividends = models.IntegerField('剰余金の配当', blank=True, null=True)  # 剰余金の配当
    share_buyback = models.IntegerField('自社株買い', blank=True, null=True)  # 自社株買い
    dividend_payout_ratio = models.FloatField('配当性向', default=118.9)  # 配当性向
    total_return_ratio = models.FloatField('総還元性向', blank=True, null=True)  # 総還元性向
    net_asset_dividend_ratio = models.FloatField('純資産配当率', blank=True, null=True)  # 純資産配当率
    result = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)  # 会社名
    proba = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(default=date.today()) #default=date.today() : 本日の日付をデフォルトに設定

    def __str__(self):
        if self.proba == 0.0:
            return f'[{self.id}][{self.registered_date.strftime('%Y/%m/%d %H:%M:%S')}] {self.company_name} ({self.code}) - FY{self.year}'
        else:
            return f'[{self.id}][{self.registered_date.strftime('%Y/%m/%d %H:%M:%S')}] {self.company_name} ({self.code}) - FY{self.year}'
