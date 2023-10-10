from django.contrib import admin
from .models import Student4
# Register your models here.

@admin.register (Student4)
class StudentAdmin (admin.ModelAdmin) :
    list_display = ['id', 'name','roll', 'city']