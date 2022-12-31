from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from nsepython import *

from .utils import *

NEWS_URL = "https://www.moneycontrol.com/news/business/markets/"
MARKET_TURNOVER_URL = "https://www.moneycontrol.com/stocksmarketsindia/"
ADR_GDR_URL = "https://www.goodreturns.in/adr-gdr-listings.html"
TOP_SURFERS_URL = "https://www.moneycontrol.com/stocksmarketsindia/"

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
    adr_data = scrape_adr(ADR_GDR_URL)
    data = {
        'table': adr_data
    }
    return render(request, 'adr.html', context=data)

def gdr(request):
    gdr_data = scrape_gdr(ADR_GDR_URL)
    data = {
        'table': gdr_data
    }
    return render(request, 'gdr.html', context=data)

def top_surfers(request):
    top_gainers_data = scrape_top_surfers(TOP_SURFERS_URL)
    data = {
        'table': top_gainers_data
    }
    return render(request, 'top-surfers.html', context=data)

def option_flows(request):
    option_flows_data = nse_fiidii('list')
    # print(option_flows_data)
    data = {
        'table': option_flows_data
    }
    return render(request, 'option-flows.html', context=data)