from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        read_only_fields = ('product',)  # 외래키 읽기전용 설정
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        read_only_fields = ('product',)  # 외래키 읽기전용 설정
        fields = '__all__'