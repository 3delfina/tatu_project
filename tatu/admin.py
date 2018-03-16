from django.contrib import admin
from tatu.models import * 


# Register your models here.
admin.site.register(Page)
admin.site.register(Picture)
admin.site.register(Comment)

class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 3

class UserAdmin(admin.ModelAdmin):
    inlines = [ UserImageInline, ]

admin.site.register(UserProfile, UserAdmin)
