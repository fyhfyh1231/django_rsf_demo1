from django.db import models

# Create your models here.
class band_sell(models.Model):
    band_name=models.CharField(verbose_name='品牌',max_length=50)
    month=models.IntegerField(verbose_name='月份')
    weeks=models.IntegerField(verbose_name='周数')
    month_week=models.CharField(verbose_name='月周',max_length=7)
    aidou=models.CharField(verbose_name='爱都',max_length=10)
    amount_money=models.DecimalField(verbose_name='金额占比',max_digits=6, decimal_places=2)
    amount_sales=models.DecimalField(verbose_name='销量占比',max_digits=6, decimal_places=2)
    total_money=models.DecimalField(verbose_name='销售金额',max_digits=10, decimal_places=0)
    total_sales=models.DecimalField(verbose_name='销量',max_digits=10, decimal_places=0)
    visitor=models.DecimalField(verbose_name='曝光量',max_digits=8, decimal_places=0)
    total_visitor=models.DecimalField(verbose_name='行业曝光量',max_digits=8, decimal_places=0)
    price=models.DecimalField(verbose_name='单价',max_digits=8, decimal_places=2)
    average_price=models.DecimalField(verbose_name='平均单价',max_digits=8, decimal_places=2)
    transaction=models.CharField(verbose_name='转化率',max_length=7)
    average_transaction=models.CharField(verbose_name='平均转化率',max_length=7)

