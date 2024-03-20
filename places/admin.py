from django.contrib import admin
from .models import *

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    list_editable = ('email',)  # Make sure to include a comma to make it a tuple


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'comment')
    search_fields = ('user', 'place',)
    list_editable = ('comment',)

class PlaceOwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'place',)

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceOwner, PlaceOwnerAdmin)
admin.site.register(Comment, CommentAdmin)
