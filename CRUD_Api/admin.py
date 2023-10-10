from django.contrib import admin
from .models import Student3
# Register your models here.

@admin.register (Student3)
class StudentAdmin (admin.ModelAdmin) :
    list_display = ['id', 'name','roll', 'city']