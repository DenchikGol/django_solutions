from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Problem)
admin.site.register(Symptom)
admin.site.register(Comment, MPTTModelAdmin)
