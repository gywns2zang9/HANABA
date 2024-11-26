from django.db import models

# Create your models here.
class DepositProducts(models.Model):
  dcls_month = models.TextField(null=True)  # 공시 제출월 [YYYYMM]
  fin_co_no = models.TextField()  # 금융회사 코드
  kor_co_nm = models.TextField()  # 금융회사 명
  fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
  fin_prdt_nm = models.TextField()  # 금융 상품명
  join_way = models.TextField()  # 가입 방법
  mtrt_int = models.TextField(null=True)  # 만기 후 이자율
  spcl_cnd = models.TextField()  # 우대조건
  join_deny = models.IntegerField()  # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
  join_member = models.TextField()  # 가입대상
  etc_note = models.TextField()  # 기타 유의사항
  max_limit = models.IntegerField(null=True)  # 최대 한도, null 허용
  dcls_strt_day = models.TextField(null=True)  # 공시 시작일 [YYYYMMDD]
  dcls_end_day = models.TextField(null=True)  # 공시 종료일 [YYYYMMDD], null 허용
  fin_co_subm_day = models.TextField(null=True)  # 금융회사 제출일 [YYYYMMDDHHMM]
  
class DepositOptions(models.Model):
  product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) #외래 키(DepositProducts 클래스 참조)
  dcls_month = models.TextField(null=True)  # 공시 제출월 [YYYYMM]
  fin_co_no = models.TextField()  # 금융회사 코드
  fin_prdt_cd = models.TextField() # 금융 상품 코드
  intr_rate_type = models.CharField(max_length=100) # 저축 금리 유형
  intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
  save_trm = models.IntegerField() # 저축 기간 [단위: 개월]
  intr_rate = models.FloatField(null=True) # 저축 금리 [소수점 2자리]
  intr_rate2 = models.FloatField(null=True) # 최고 우대금리 [소수점 2자리]

class SavingProducts(models.Model):
  dcls_month = models.TextField(null=True)  # 공시 제출월 [YYYYMM]
  fin_co_no = models.TextField()  # 금융회사 코드
  kor_co_nm = models.TextField()  # 금융회사 명
  fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
  fin_prdt_nm = models.TextField()  # 금융 상품명
  join_way = models.TextField()  # 가입 방법
  mtrt_int = models.TextField(null=True)  # 만기 후 이자율
  spcl_cnd = models.TextField()  # 우대조건
  join_deny = models.IntegerField()  # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
  join_member = models.TextField()  # 가입대상
  etc_note = models.TextField()  # 기타 유의사항
  max_limit = models.IntegerField(null=True)  # 최대 한도, null 허용
  dcls_strt_day = models.TextField(null=True)  # 공시 시작일 [YYYYMMDD]
  dcls_end_day = models.TextField(null=True)  # 공시 종료일 [YYYYMMDD], null 허용
  fin_co_subm_day = models.TextField(null=True)  # 금융회사 제출일 [YYYYMMDDHHMM]
  

class SavingOptions(models.Model):
  product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE) #외래 키(SavingProducts 클래스 참조)
  dcls_month = models.TextField()  # 공시 제출월 [YYYYMM]
  fin_co_no = models.TextField()  # 금융회사 코드
  fin_prdt_cd = models.TextField() # 금융 상품 코드
  intr_rate_type = models.CharField(max_length=100) # 저축 금리 유형
  intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
  rsrv_rate_type = models.CharField(max_length=100, null=True) # 적립 유형
  rsrv_rate_type_nm = models.CharField(max_length=100, null=True) # 적립 유형명
  save_trm = models.IntegerField() # 저축 기간 [단위: 개월]
  intr_rate = models.FloatField(null=True) # 저축 금리 [소수점 2자리]
  intr_rate2 = models.FloatField(null=True) # 최고 우대금리 [소수점 2자리]