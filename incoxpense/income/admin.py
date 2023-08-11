from django.contrib import admin
from .models import Income, Source
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'source', 'date',)
    search_fields = ('description', 'source', 'date',)

    list_per_page = 5

admin.site.register(Income,IncomeAdmin)
admin.site.register(Source)