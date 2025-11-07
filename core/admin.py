from django.contrib import admin
from .models import CostomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CostomUser)
class CustomUSerAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info",{"fields":("phone_number",)}),
    )