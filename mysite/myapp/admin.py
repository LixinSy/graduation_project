from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Album)
admin.site.register(models.Photo)
admin.site.register(models.AlbumTag)
admin.site.register(models.AlbumComment)
admin.site.register(models.Favour)
admin.site.register(models.Collection)