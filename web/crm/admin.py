from django.contrib import admin

from .models import Customer, Note


class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
    readonly_fields = ["content"]


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer', {'fields': [
            'first_name', 
            'last_name', 
            'address', 
            'city', 
            'state', 
            'zip_code', 
            'primary_phone', 
            'secondary_phone'
        ]}),
    ]
    inlines = [NoteInline]
    list_display = ('first_name', 'last_name', 'city', 'state')
    search_fields = ['first_name', 'last_name']





admin.site.register(Customer, CustomerAdmin)
admin.site.register(Note)
