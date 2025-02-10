from django.shortcuts import render, redirect
from .forms import InputForm, LoginForm
from .models import StockStatement
import requests
from bs4 import BeautifulSoup

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'twoxstockfinderapp/index.html')

@login_required
def input_form(request):
    if request.method == "POST": # Formの入力があった時、
        form = InputForm(request.POST) # 入力データを取得する。
        if form.is_valid(): # Formの記載の検証を行い、
            form.save() # 問題なければ、入力データを保存
            return redirect('result') # 保存後遷移するページの指定
    else:
        form = InputForm()
        return render(request, 'twoxstockfinderapp/input_form.html', {'form':form})

@login_required
def result(request):
    # 最新の登録者のデータを取得
    statement = StockStatement.objects.order_by('id').reverse().first()

    # 推論の実行 (APIへリクエスト)
    x = {
        "bps": float(statement.bps) if statement.bps is not None else None,
        "long_term_loans": float(statement.long_term_loans) if statement.long_term_loans is not None else None,
        "dividend_payout_ratio": float(statement.dividend_payout_ratio) if statement.dividend_payout_ratio is not None else None,
        "revenue": float(statement.revenue) if statement.revenue is not None else None,
        "roe": float(statement.roe) if statement.roe is not None else None,
        "investing_cf": float(statement.investing_cf) if statement.investing_cf is not None else None,
        "operating_cf_margin": float(statement.operating_cf_margin) if statement.operating_cf_margin is not None else None,
        "financing_cf": float(statement.financing_cf) if statement.financing_cf is not None else None,
        "shareholders_equity": float(statement.shareholders_equity) if statement.shareholders_equity is not None else None,
        "retained_earnings": float(statement.retained_earnings) if statement.retained_earnings is not None else None,
        "cash_equivalents": float(statement.cash_equivalents) if statement.cash_equivalents is not None else None,
        "roa": float(statement.roa) if statement.roa is not None else None,
        "dividend_per_share": float(statement.dividend_per_share) if statement.dividend_per_share is not None else None,
        "retained_earnings_dividends": float(statement.retained_earnings_dividends) if statement.retained_earnings_dividends is not None else None,
        "net_assets": float(statement.net_assets) if statement.net_assets is not None else None,
        "total_assets": float(statement.total_assets) if statement.total_assets is not None else None,
        "net_income": float(statement.net_income) if statement.net_income is not None else None,
        "ordinary_income": float(statement.ordinary_income) if statement.ordinary_income is not None else None,
        "net_asset_dividend_ratio": float(statement.net_asset_dividend_ratio) if statement.ordinary_income is not None else None,
        "equity_ratio": float(statement.equity_ratio) if statement.equity_ratio is not None else None,
        "operating_income": float(statement.operating_income) if statement.operating_income is not None else None,
        "total_return_ratio": float(statement.total_return_ratio) if statement.total_return_ratio is not None else None,
        "short_term_loans": float(statement.short_term_loans) if statement.short_term_loans is not None else None,
        "capital_expenditure": float(statement.capital_expenditure) if statement.capital_expenditure is not None else None,
        "eps": float(statement.eps) if statement.eps is not None else None,
        "share_buyback": float(statement.share_buyback) if statement.share_buyback is not None else None,
        "operating_cf": float(statement.operating_cf) if statement.operating_cf is not None else None,
    }
    response = requests.post("https://twoxstockfinderapi.onrender.com/make_predictions", json=x)
    y = response.json()["predict"]
    y_proba = response.json()["proba"]

    # 推論結果を保存
    statement.company_name, current_price = get_company_name_and_current_price(statement.code)
    statement.proba = round(y_proba*100, 2)
    statement.result = y
    statement.save() # データを保存

    # 推論結果をHTMLに渡す
    result = {
        'company_name': statement.company_name,
        'code': statement.code,
        'year': statement.year,
        'result': statement.result,
        'proba': statement.proba,
        'current_price': current_price,
    }
    return render(request, 'twoxstockfinderapp/result.html', result)

def get_company_name_and_current_price(code):
    response = requests.get(f'https://kabutan.jp/stock/kabuka?code={code}&ashi=yar')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', class_='si_i1_1')
        company_name = div.find('h2').text.replace(f'{code}　', '').strip()
        price = soup.find('span', class_='kabuka').text.replace('円', '').strip()
    return company_name, float(price.replace(',', ''))

@login_required
def history(request):
    if request.method == 'POST':
        d_id = request.POST # POSTされた値を取得→ID
        d_statement = StockStatement.objects.filter(id=d_id['d_id']) # filterメソッドでidが一致するStockStatementのデータを取得
        d_statement.delete() # 取得した決算データを消去
        statements = StockStatement.objects.all() # 決算全データを取得
        return render(request, 'twoxstockfinderapp/history.html', {'statements':statements})
    else:
        statements = StockStatement.objects.all()
        return render(request, 'twoxstockfinderapp/history.html', {'statements':statements})

class Login(LoginView):
    form_class = LoginForm
    template_name = 'twoxstockfinderapp/login.html'

class Logout(LogoutView):
    template_name = 'twoxstockfinderapp/base.html'
