from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    if 'stockid' in request.GET:
        stockid = request.GET['stockid']
    else:
        stockid = ''
    print(stockid)
    return render(request, 'home.html', {'stockid': stockid})

def aboutpage(request):
    return render(request, 'about.html')

def result(request):
    return render(request, 'result.html')
