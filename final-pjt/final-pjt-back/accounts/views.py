from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404 # type: ignore
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer
from products.models import DepositProducts, SavingProducts
# Create your views here.

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info(request):
    username = request.user.username
  # if request.user.username == username:
    user = get_object_or_404(get_user_model(), username=username)
    deposit_product_pks = user.deposit_products.values_list('pk', flat=True)
    deposit_product_names = DepositProducts.objects.filter(pk__in=deposit_product_pks).values_list('fin_prdt_nm', flat=True)
    
    saving_product_pks = user.saving_products.values_list('pk', flat=True)
    saving_product_names = SavingProducts.objects.filter(pk__in=saving_product_pks).values_list('fin_prdt_nm', flat=True)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        additional_data = {
            'deposit_product_names': list(deposit_product_names),
            'saving_product_names': list(saving_product_names),
        }
        response_data = {**serializer.data, **additional_data}
        return Response(response_data)
      
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_deposit(request, fin_prdt_cd):
  deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
  # 사용자가 이미 해당 상품을 가입한 경우
  if request.user.deposit_products.filter(fin_prdt_cd=fin_prdt_cd).exists():
      request.user.deposit_products.remove(deposit_product)
      return Response({"message": "해당 예금 상품을 가입 해제했습니다."}, status=status.HTTP_200_OK)
  else:
      request.user.deposit_products.add(deposit_product)
      return Response({"message": "해당 예금 상품을 가입했습니다."}, status=status.HTTP_201_CREATED)
      
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_saving(request, fin_prdt_cd):
  saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
  # 사용자가 이미 해당 상품을 가입한 경우
  if request.user.saving_products.filter(fin_prdt_cd=fin_prdt_cd).exists():
      request.user.saving_products.remove(saving_product)
      return Response({"message": "해당 적금 상품을 가입 해제했습니다."}, status=status.HTTP_200_OK)
  else:
      request.user.saving_products.add(saving_product)
      return Response({"message": "해당 적금 상품을 가입했습니다."}, status=status.HTTP_201_CREATED)