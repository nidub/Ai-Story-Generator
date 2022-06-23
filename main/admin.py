from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(entries)
admin.site.register(stories)
admin.site.register(generated)