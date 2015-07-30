from django.db import models

# Create your models here.

class XiaoHuaGongYi(models.Model):
    '''
    '''
    xiaohua_name = models.CharField(max_length=100, default='xiaohua')
    money_quota = models.CharField(max_length=20, default='0')
    money_get = models.CharField(max_length=20, default='0')

    xiaohua_story = models.TextField(default='')

    xiaohua_pic_list = models.TextField(default='')
