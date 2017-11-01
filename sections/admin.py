from django.contrib import admin
from .models import *

class WorkImageInline(admin.StackedInline):
    model = Work_Image
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    inlines = [WorkImageInline]

admin.site.register(Content)
admin.site.register(Experience)
admin.site.register(Work, WorkAdmin)
