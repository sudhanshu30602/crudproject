from django.contrib import admin
from crudapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid', 'ename', 'eemail', 'econtact', 'epassword')

admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
