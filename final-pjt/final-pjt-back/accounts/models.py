from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import DepositProducts, SavingProducts

# Create your models here.
class User(AbstractUser):
    deposit_products = models.ManyToManyField(DepositProducts)
    saving_products = models.ManyToManyField(SavingProducts)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.TextField(blank=True, null=True)
    asset = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    target_period = models.IntegerField(blank=True, null=True)
    future_value = models.IntegerField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
