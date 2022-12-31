from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name="news"),
    path('marketTurnover/', market_turnover, name="market-turnover"),
    path('adr/', adr, name="adr"),
    path('gdr/', gdr, name="gdr"),
    path('topSurfers/', top_surfers, name="top-surfers"),
    path('optionFlows/', option_flows, name="option-flows"),
]