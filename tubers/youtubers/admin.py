from django.contrib import admin

from .models import Youtuber
# Register your models here

from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src ="{}"  width="40" />'.format(object.photo.url))

    #overwritng some lists
    list_display = ('id', 'name', 'myphoto', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type') #helps us to search based on only roles or first names in the search box
    list_filter = ('city', 'camera_type')  #helps filter out objects with same group
    list_display_links = ('name', 'id')   #what fields are to be given clickable links
    list_editable = ('is_featured', )    #what feilds shoulld be editable directly from the outer view

admin.site.register(Youtuber, YtAdmin)