from django.contrib import admin
from gpuApi.models import Product
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Product)


@admin.register(Product)
class ViewAdmin(ImportExportModelAdmin):
    pass
