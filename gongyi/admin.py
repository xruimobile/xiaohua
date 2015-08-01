from django.contrib import admin
from gongyi.models import Children

# Register your models here.

class ChildrenAdmin(admin.ModelAdmin):
    pass

admin.site.register(Children, ChildrenAdmin)
