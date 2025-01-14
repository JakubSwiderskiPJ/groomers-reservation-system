from django.contrib import admin
from .models import Employee, Customer, Dog, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')  # Fields to display in admin list view
    search_fields = ('name', 'position')  # Fields to allow searching
    list_filter = ('position',)  # Filter by position

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'dog_name')  # Fields to display in admin list view
    search_fields = ('name', 'phone', 'dog_name')  # Fields to allow searching

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed','owner','note', 'last_visit')  # Fields to display in admin list view
    search_fields = ('name', 'breed', 'owner__name')  # Search by dog name, breed, and owner's name
    list_filter = ('breed',)  # Filter by breed

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'customer', 'purpose')  # Display these fields
    search_fields = ('dog__name', 'customer__name', 'employee__name', 'purpose')  # Allow searching
    list_filter = ('date', 'time',)  # Filter by date, time, and employee

