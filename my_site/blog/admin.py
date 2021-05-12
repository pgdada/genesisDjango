from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(School)
admin.site.register(Certificate)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
