from django.urls import path
from . import views

urlpatterns = [
    # 환율데이터를 DB에 저장
    path('save-exchange-rates/', views.save_exchange_rates, name='save_exchange_rates'),
]
