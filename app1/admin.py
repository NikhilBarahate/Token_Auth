from django.contrib import admin
from app1.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn', 'name', 'marks', 'mail']

admin.site.register(Students, StudentAdmin)