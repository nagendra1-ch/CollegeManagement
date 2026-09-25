from django.contrib import admin
from . models import Faculty,User,Student
# Register your models here.

admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Student)