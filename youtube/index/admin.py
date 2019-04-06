from django.contrib import admin

# Register your models here.

from index.models import Notes,Liked

admin.site.register(Notes)
admin.site.register(Liked)
