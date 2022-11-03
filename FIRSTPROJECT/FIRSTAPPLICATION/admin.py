from django.contrib import admin
from .models import Signup,Login,Student

# Register your models here.

#admin.site.register(Signup)
admin.site.register(Login)
admin.site.register(Student)


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
       list_display = [ 'Id','Name','Contact', 'Address']