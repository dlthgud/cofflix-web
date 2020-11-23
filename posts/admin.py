from django.contrib import admin

# Register your models here.
from .models import Cafe, Tag

admin.site.register(Cafe)
admin.site.register(Tag)
