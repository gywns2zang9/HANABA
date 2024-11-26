from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 / 적금 상품 목록 DB에 저장 
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    # 정기예금 / 적금 상품의 옵션 데이터를 가져옴
    path('get-deposit-options/<str:fin_prdt_cd>/', views.get_deposit_options, name='get_deposit_options'),
    path('get-saving-options/<str:fin_prdt_cd>/', views.get_saving_options, name='get_saving_options'),
    # 가입자 수 세기
    path('deposit-joins/<int:deposit_pk>/', views.deposit_joins, name='deposit_joins'),
    path('saving-joins/<int:saving_pk>/', views.saving_joins, name='saving_joins'),
    # 상품 추천
    path('top-deposit-products/', views.top_deposit_products, name='top_deposit_products'),
    path('top-saving-products/', views.top_saving_products, name='top_saving_products'),
]