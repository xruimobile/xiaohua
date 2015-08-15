# -*- coding:utf-8 -*-
from django.contrib import admin
from gongyi.models import Children, ChildDream

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

    def icon_disable(self, obj):
        # return '<a href="%s" target="_blank">%s</a>' % (obj.icon.name, obj.icon.name)
        return '<a href="%s" target="_blank">%s</a>' % (obj.icon, obj.icon)
    icon_disable.short_description = '头像'
    icon_disable.allow_tags = True

    def icon_preview(self, obj):
        # return '<img id="id_icon_preview" src="%s" style="max-height:180px;max-width:320px;%s"/>' % (
        #     obj.icon.name or '', "" if obj.icon else 'display:none;')
        return '<img id="id_icon_preview" src="%s" style="max-height:180px;max-width:320px;%s"/>' % (
            obj.icon or '', "" if obj.icon else 'display:none;')

    icon_preview.allow_tags = True


class ChildDreamAdmin(admin.ModelAdmin):
    list_display = ['child_id',
                    'donate_type',
                    'dream',
                    'status']

admin.site.register(ChildDream, ChildDreamAdmin)
admin.site.register(Children, ChildrenAdmin)
