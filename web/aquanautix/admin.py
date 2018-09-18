from django.contrib import admin

from .models import Artifact, Picture


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 3


class ArtifactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]
    inlines = [PictureInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(Picture)
