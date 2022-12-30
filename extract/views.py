from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .utils import *

NEWS_URL = "https://www.moneycontrol.com/news/business/markets/"
MARKET_TURNOVER_URL = "https://www.moneycontrol.com/stocksmarketsindia/"
ADR_GDR_URL = "https://www.goodreturns.in/adr-gdr-listings.html"

# Create your views here.

def news(request):
    news_data = scrape_news(NEWS_URL)
    data = {
        'news': news_data
    }
    return render(request, 'news.html', context=data)


def market_turnover(request):
    market_turnover_data = scrape_market_turnover(MARKET_TURNOVER_URL)
    data = {
        'table': market_turnover_data
    }
    return render(request, 'market-turnover.html', context=data)

def adr(request):
    adr_data = scrape_adr()