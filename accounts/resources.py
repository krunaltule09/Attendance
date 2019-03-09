from import_export import resources
from django.contrib.auth import get_user_model
from .models import Student

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


User=get_user_model()
class UserResource(resources.ModelResource):
    class Meta:
        model = User