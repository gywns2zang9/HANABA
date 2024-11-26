import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts
from accounts.models import User
from django.db.models import Count
from django.db.models import F
from django.db.models.functions import Abs
# Create your views here.
PRODUCT_API_KEY = settings.PRODUCT_API_KEY

@api_view(['GET'])
def save_deposit_products(request):
    """
    정기예금 상품 목록을 API에서 가져와 DB에 저장하는 함수입니다.
    """
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')

    # Base 데이터 저장
    for base_data in response.get('baseList'):
        fin_prdt_cd = base_data.get('fin_prdt_cd')

        # 이미 DB에 존재하는 데이터인지 확인 후 저장
        if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            serializer = DepositProductsSerializer(data=base_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    # Option 데이터 저장
    for option_data in response.get('optionList'):
        fin_prdt_cd = option_data.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

        # 모든 필드가 같은 데이터가 이미 존재하는지 확인 후 저장
        if not DepositOptions.objects.filter(
            product=product,
            intr_rate_type=option_data.get('intr_rate_type'),
            intr_rate_type_nm=option_data.get('intr_rate_type_nm'),
            save_trm=option_data.get('save_trm'),
            intr_rate=option_data.get('intr_rate'),
            intr_rate2=option_data.get('intr_rate2')
        ).exists():
            serializer = DepositOptionsSerializer(data=option_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)

    # 데이터 저장 후 전체 데이터를 응답으로 반환
    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposit_products, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def save_saving_products(request):
    """
    적금 상품 목록을 API에서 가져와 DB에 저장하는 함수입니다.
    """
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')

    # Base 데이터 저장
    for base_data in response.get('baseList'):
        fin_prdt_cd = base_data.get('fin_prdt_cd')

        # 이미 DB에 존재하는 데이터인지 확인 후 저장
        if not SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            serializer = SavingProductsSerializer(data=base_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    # Option 데이터 저장
    for option_data in response.get('optionList'):
        fin_prdt_cd = option_data.get('fin_prdt_cd')
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

        # 모든 필드가 같은 데이터가 이미 존재하는지 확인 후 저장
        if not SavingOptions.objects.filter(
            product=product,
            intr_rate_type=option_data.get('intr_rate_type'),
            intr_rate_type_nm=option_data.get('intr_rate_type_nm'),
            rsrv_rate_type=option_data.get('rsrv_rate_type'),
            rsrv_rate_type_nm=option_data.get('rsrv_rate_type_nm'),
            save_trm=option_data.get('save_trm'),
            intr_rate=option_data.get('intr_rate'),
            intr_rate2=option_data.get('intr_rate2')
        ).exists():
            serializer = SavingOptionsSerializer(data=option_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)

    # 데이터 저장 후 전체 데이터를 응답으로 반환
    saving_products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(saving_products, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_deposit_options(request, fin_prdt_cd):
    """
    특정 예금 상품의 옵션을 검색하여 반환하는 함수
    """
    deposit_options = DepositOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_saving_options(request, fin_prdt_cd):
    """
    특정 적금 상품의 옵션을 검색하여 반환하는 함수
    """
    saving_options = SavingOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(saving_options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_joins(request, deposit_pk):
    # DepositProducts 객체 가져오기
    deposit_product = DepositProducts.objects.get(pk=deposit_pk)

    # 해당 상품에 가입한 사용자 수 가져오기
    num_users = deposit_product.user_set.count()
    return JsonResponse({'num_users': num_users})

@api_view(['GET'])
def saving_joins(request, saving_pk):
    saving_product = SavingProducts.objects.get(pk=saving_pk)
    num_users = saving_product.user_set.count()
    return JsonResponse({'num_users': num_users})

@api_view(['GET'])
def top_deposit_products(request):
    user_age = request.user.age
    users_within_age_range = User.objects.annotate(age_diff=Abs(F('age') - user_age)).filter(age_diff__lte=5)
    deposit_products = DepositProducts.objects.filter(user__in=users_within_age_range)
    product_count = deposit_products.values('fin_prdt_cd', 'fin_prdt_nm').annotate(count=Count('fin_prdt_cd')).order_by('-count')
    top_products = product_count[:3]  # 상위 3개 상품
    
    return Response(top_products)

@api_view(['GET'])
def top_saving_products(request):
    user_age = request.user.age
    users_within_age_range = User.objects.annotate(age_diff=Abs(F('age') - user_age)).filter(age_diff__lte=5)
    saving_products = SavingProducts.objects.filter(user__in=users_within_age_range)
    product_count = saving_products.values('fin_prdt_cd', 'fin_prdt_nm').annotate(count=Count('fin_prdt_cd')).order_by('-count')
    top_products = product_count[:3]  # 상위 3개 상품
    
    return Response(top_products)