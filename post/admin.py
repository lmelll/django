from django.contrib import admin

from .models import Thing
 
class ThingModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"text", "id"]
    list_display_links = ["id"]
    list_editable = ["text"]
    list_filter = ["id"]
    search_fields = ["text"]
 
admin.site.register(Thing, ThingModelAdmin)