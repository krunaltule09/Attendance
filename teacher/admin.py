
from django.contrib import admin
from .models import Teacher,SecretCode
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resources import TeacherResource



class TeacherModelAdmin(ImportExportModelAdmin):
    resource_class = TeacherResource
    pass

admin.site.register(Teacher,TeacherModelAdmin)
admin.site.register(SecretCode)
