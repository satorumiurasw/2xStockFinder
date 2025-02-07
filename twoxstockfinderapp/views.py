from django.shortcuts import render
from django.http import HttpResponse # モジュールの読み込み

def hellofunction(request):
    return render(request, 'twoxstockfinderapp/hello.html')
