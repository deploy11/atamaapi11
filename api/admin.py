from django.contrib import admin
from .models import *
from .resorses import ResultResorces
from import_export.admin import ImportExportModelAdmin
# Register your models here.]
class ResultAdmin(ImportExportModelAdmin):
    list_display = ['nomi','type','uzb','rus','eng']
    resource_class = ResultResorces
admin.site.register(Atama,ResultAdmin)