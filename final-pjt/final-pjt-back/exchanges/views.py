import requests
from datetime import date
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ExchangeRatesSerializer
from .models import ExchangeRates
from rest_framework.exceptions import APIException

EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
EXCHANGE_API_URL = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

@api_view(['GET'])
def save_exchange_rates(request):
    # 오늘 날짜 구하기
    # today = date.today().strftime("%Y%m%d")
    # API 요청 시 사용할 파라미터 설정
    params = {
        'authkey': EXCHANGE_API_KEY,
        'searchdate': "20240522", # 일단 오늘 날짜로 저장
        'data': 'AP01'
    }
    # API에 요청 보내기
    response = requests.get(EXCHANGE_API_URL, params=params)

    if response.ok:
        exchange_data = response.json()  # JSON 데이터를 딕셔너리로 파싱

        # 이전 데이터 삭제
        ExchangeRates.objects.all().delete()
        
        # 받아온 데이터를 모델에 저장
        for rate in exchange_data:
            serializer = ExchangeRatesSerializer(data=rate)
            if serializer.is_valid():
                serializer.save()
            else:
                # 유효하지 않은 데이터는 로그에 남기거나 다른 처리 수행
                pass

        # 데이터베이스에 저장된 모든 환율 데이터를 가져옴
        exchange_rates = ExchangeRates.objects.all()
        # 직렬화
        serializer = ExchangeRatesSerializer(exchange_rates, many=True)
        # 직렬화된 데이터를 JSON 형식으로 반환
        return Response(serializer.data)
    else:
        raise APIException(detail="Failed to fetch exchange rates.")