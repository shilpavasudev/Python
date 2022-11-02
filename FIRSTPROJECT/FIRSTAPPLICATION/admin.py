from django.contrib import admin
from .models import Signup
# Register your models here.

#admin.site.register(Signup)

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = [ 'id','Name','Contact', 'Address']