from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_name', 'department', 'designation', 'salary', 'date_of_joining')
    search_fields = ('full_name', 'department')
    list_filter = ('department', 'designation')
