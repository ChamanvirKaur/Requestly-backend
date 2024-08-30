from django.contrib import admin
from .models import Branch

class BranchView(admin.ModelAdmin):
    list_display = ('branch_number', 'branch_name', 'branch_address', 'branch_phone')
    search_fields = ('branch_number','branch_name','branch_city')
    list_filter=('branch_number',)
    list_per_page = 30
    ordering=['branch_number']

admin.site.register(Branch,BranchView)

