from django.contrib import admin
from gongyi.models import Children, ChildDream

# Register your models here.

class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'age',
                    'icon',
                    'status']

    readonly_fields = ['icon_preview']

    def icon_preview(self, obj):
        return '<img src="%s" style="max-height:180px;max-width:320px;%s"/>' % (
            obj.icon.name or '', "" if obj.icon else 'display:none;')

    icon_preview.allow_tags = True


class ChildDreamAdmin(admin.ModelAdmin):
    list_display = ['child_id',
                    'donate_type',
                    'dream',
                    'status']

admin.site.register(ChildDream, ChildDreamAdmin)
admin.site.register(Children, ChildrenAdmin)
