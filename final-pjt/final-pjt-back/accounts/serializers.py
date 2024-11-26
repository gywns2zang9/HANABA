from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=50)
    asset = serializers.IntegerField()
    salary = serializers.IntegerField()
    target_period = serializers.IntegerField()
    future_value = serializers.IntegerField()
    purpose = serializers.CharField(max_length=50)

    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.age = self.data.get('age')
        user.gender = self.data.get('gender')
        user.asset = self.data.get('asset')
        user.salary = self.data.get('salary')
        user.target_period = self.data.get('target_period')
        user.future_value = self.data.get('future_value')
        user.purpose = self.data.get('purpose')
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'age', 'gender', 'asset', 'salary', 'target_period', 'future_value', 'purpose', 'deposit_products', 'saving_products')