from django.contrib import admin
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportModelAdmin
from .resources import StudentResource,UserResource
from import_export import resources
from .models import Subject,Panel

# from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User=get_user_model()

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email','admin','username')
#     list_filter = ('admin', 'staff', 'active','verified')
#     fieldsets = (
#         (None, {'fields': ('username','password')}),
#         ('Personal info', {'fields': ('email',)}),
#         ('Permissions', {'fields': ('admin', 'staff', 'active','verified')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email','username','password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

#--------------- for import export stuff---------------------

class UserModelAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    pass


# ---------------------------------------------------------
# admin.site.register(UserModelAdmin)
admin.site.register(User,UserModelAdmin)
admin.site.register(Subject)
admin.site.register(Panel)






