from django.contrib import admin
from .models import Customs
# Register your models here.
class CustomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','title', 'desc', 'refimg')
    #list_display_links = ('id', '')
    list_editable = ('desc',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Customs,CustomsAdmin)
  