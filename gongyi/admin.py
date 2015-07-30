from django.contrib import admin
from gongyi.models import XiaoHuaGongYi

# Register your models here.

class XiaoHuaGongYiAdmin(admin.ModelAdmin):
    list_display = ['xiaohua_name',
                    'money_quota',
                    'money_get',
                    'donate_num']

admin.site.register(XiaoHuaGongYi, XiaoHuaGongYiAdmin)
