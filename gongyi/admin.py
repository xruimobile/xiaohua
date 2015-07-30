from django.contrib import admin
from gongyi.models import XiaoHuaGongYi

# Register your models here.

class XiaoHuaGongYiAdmin(admin.ModelAdmin):
    pass

admin.site.register(XiaoHuaGongYi, XiaoHuaGongYiAdmin)
