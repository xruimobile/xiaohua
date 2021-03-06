# -*- coding:utf-8 -*-
from django.contrib import admin
from gongyi.models import Children, ChildDream, RecommendUser, UserInfo

# Register your models here.

class ChildrenAdmin(admin.ModelAdmin):

    class Media:
        js = ("js/file_upload_editor.js", )

    list_display = ['name',
                    'age',
                    'icon_disable',
                    'status']

    readonly_fields = ['icon_preview',
                       'sound_id']

    search_fields = ['name']

    actions = ['put_online',
               'put_offline']

    def icon_disable(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.icon, obj.icon)
    icon_disable.short_description = '头像'
    icon_disable.allow_tags = True

    def icon_preview(self, obj):
        # return '<img id="id_icon_preview" src="%s" style="max-height:180px;max-width:320px;%s"/>' % (
        #     obj.icon.name or '', "" if obj.icon else 'display:none;')
        return '<img id="id_icon_preview" src="%s" style="max-height:180px;max-width:320px;%s"/>' % (
            obj.icon or '', "" if obj.icon else 'display:none;')
    icon_preview.short_description = '头像预览'
    icon_preview.allow_tags = True

    def put_online(modeladmin, request, queryset):
        queryset.update(status='1')
    put_online.short_description = '上线'

    def put_offline(modeladmin, request, queryset):
        queryset.update(status='0')
    put_offline.short_description = '下线'


class ChildDreamAdmin(admin.ModelAdmin):
    list_display = ['child',
                    'donate_type',
                    'dream',
                    'status']

    raw_id_fields = ['child']

    search_fields = ['child__name']

    actions = ['put_online',
               'put_offline']

    def put_online(modeladmin, request, queryset):
        queryset.update(status='1')
    put_online.short_description = '上线'

    def put_offline(modeladmin, request, queryset):
        queryset.update(status='0')
    put_offline.short_description = '下线'

admin.site.register(ChildDream, ChildDreamAdmin)
admin.site.register(Children, ChildrenAdmin)



class RecommendUserAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name']

    def name(self, obj):
        return UserInfo.objects.get(uid=obj.uid).name

    name.short_description = '姓名'

admin.site.register(RecommendUser, RecommendUserAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name']
    search_fields = ['name']
    actions = ['recommend']
    list_per_page = 30

    def recommend(modeladmin, request, queryset):
        for user in queryset:
            RecommendUser.objects.get_or_create(uid=user.uid)
    recommend.short_description = '推荐展示'

admin.site.register(UserInfo, UserInfoAdmin)
