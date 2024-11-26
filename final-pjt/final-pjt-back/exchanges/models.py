from django.db import models

# Create your models here.
class ExchangeRates(models.Model):
    result = models.IntegerField() # 조회 결과
    cur_unit = models.TextField() # 통화코드
    ttb = models.TextField() # 전신환(송금)받으실때
    tts = models.TextField() # 전신환(송금)보내실때
    deal_bas_r = models.TextField() # 매매 기준율	
    bkpr = models.TextField() # 장부가격
    yy_efee_r = models.TextField() # 년환가료율
    ten_dd_efee_r = models.TextField() # 10일환가료율	
    kftc_bkpr = models.TextField() # 서울외국환중개 매매기준율
    kftc_deal_bas_r = models.TextField() # 서울외국환중개 장부가격
    cur_nm = models.TextField() # 국가/통화명