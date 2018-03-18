from django.contrib import admin
from imagekit.admin import AdminThumbnail
from tatu.models import * 

admin.site.register(Page)
admin.site.register(Comment)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='avatar')

admin.site.register(UserProfile, PhotoAdmin)
