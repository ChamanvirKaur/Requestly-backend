from django.contrib import admin
from .models import UserDetail, ticket
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserDetail
    list_display =('id','email','first_name', 'last_name','phone', 'province','modified_on')
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("email", "password1", "password2", "first_name","last_name","phone","street_address","province"),
                },
            ),
        )
    fieldsets=UserAdmin.fieldsets
    list_display_links=('id','email','phone')
    search_fields = ('email','first_name','last_name','phone')
    list_per_page = 30
    ordering =['-id']

class TicketView(admin.ModelAdmin):
    list_display=('id','ticket_type','created_by', 'ticket_state','estimated_completion','modified_on','created_on','requested_branch')
    search_fields=('ticket_number', 'ticket_type','ticket_state',)
    list_per_page= 30
    ordering=['-id']

admin.site.register(UserDetail, CustomUserAdmin)
admin.site.register(ticket,TicketView)

admin.site.unregister(Group)
Group._meta.verbose_name_plural = 'Groups/Brand'
admin.site.register(Group)

