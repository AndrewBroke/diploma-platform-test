from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(SimpleQuestion)
admin.site.register(SimpleAnswer)
admin.site.register(Measure)
admin.site.register(Test2Relations)
admin.site.register(Profile)
admin.site.register(Theme)
admin.site.register(Theory)