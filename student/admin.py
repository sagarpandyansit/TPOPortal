from django.contrib import admin

## Import models
from .models import StudentLogin, StudentApplicationForm, TPO

## This class help to make better understandable table in admin panel.
class AdminStudentLogin(admin.ModelAdmin):
    list_display = ['pk', '__str__']

# Modeel registration.
admin.site.register(StudentLogin, AdminStudentLogin)
admin.site.register(StudentApplicationForm, AdminStudentLogin)
admin.site.register(TPO, AdminStudentLogin)