from django.contrib import admin
from .models import Student
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resources import StudentResource



class StudentModelAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    pass

admin.site.register(Student,StudentModelAdmin)
