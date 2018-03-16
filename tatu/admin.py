from django.contrib import admin
from tatu.models import Page, UserProfile, Picture, Comment


# Register your models here.
admin.site.register(Page)
admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Comment)

#class PageAdmin(admin.ModelAdmin):
#    list_display = ('title', 'category', 'url')

#admin.site.register(Page, PageAdmin)
