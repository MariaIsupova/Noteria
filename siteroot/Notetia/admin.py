from django.contrib import admin
from django.contrib import admin
# from django.db.models import Max, F
from .models import *
admin.site.register(Category)
admin.site.register(Note)
# Register your models here.