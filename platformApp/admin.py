from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(SimpleQuestion)
admin.site.register(SimpleAnswer)