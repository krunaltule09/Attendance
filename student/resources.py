from import_export import resources
from student.models import Student

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
