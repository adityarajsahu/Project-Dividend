from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name="news"),
    path('marketTurnover/', market_turnover, name="market-turnover"),
]