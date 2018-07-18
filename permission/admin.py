from django.contrib import admin
from .models import Category, Employee, Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Permission)

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
