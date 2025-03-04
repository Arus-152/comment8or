from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
# Register your models here.
class C8AdminSite(AdminSite):
    site_header = "c8admin"
    site_title = "c8admin"
    index_title = "Welcome to c8admin Dashboard"
    logout_template = "comment8or/logged_out.html"

admin_site = C8AdminSite(name="c8admin")

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
