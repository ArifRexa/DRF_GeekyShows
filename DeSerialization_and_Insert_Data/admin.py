from django.contrib import admin
from .models import Student2
# Register your models here.

@admin.register (Student2)
class StudentAdmin (admin.ModelAdmin) :
    list_display = ['id', 'name','roll', 'city']