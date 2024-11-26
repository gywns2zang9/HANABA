from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info),
    path('join-deposit/<str:fin_prdt_cd>/', views.join_deposit),
    path('join-saving/<str:fin_prdt_cd>/', views.join_saving),
]