from django.contrib import admin
from .models import Branch

class BranchView(admin.ModelAdmin):
    list_display = ('branch_number', 'branch_name', 'branch_address', 'branch_phone')
    search_field = ('branch_number','branch_name','branch_city')
    list_per_page = 30

admin.site.register(BranchView,Branch)

