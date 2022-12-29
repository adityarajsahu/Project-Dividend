from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .utils import scrap_news

NEWS_URL = "https://www.moneycontrol.com/news/business/markets/"

# Create your views here.
def index(request):
    news_data = scrap_news(NEWS_URL)
    data = {
        'news': news_data
    }
    return render(request, 'index.html', context=data)