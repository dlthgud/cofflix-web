from django.contrib import admin

# Register your models here.
from .models import Cafe, Tag, Image

admin.site.register(Cafe)
admin.site.register(Tag)
admin.site.register(Image)

