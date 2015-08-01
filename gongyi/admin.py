from django.contrib import admin
from gongyi.models import Children, ChildDream

# Register your models here.

class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'age',
                    'icon',
                    'status']

class ChildDreamAdmin(admin.ModelAdmin):
    list_display = ['child_id',
                    'donate_type',
                    'dream',
                    'status']

admin.site.register(ChildDream, ChildDreamAdmin)
admin.site.register(Children, ChildrenAdmin)
