from django.contrib import admin
from gongyi.models import Children

# Register your models here.

class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'age',
                    'icon',
                    'status']

admin.site.register(Children, ChildrenAdmin)
