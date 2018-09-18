from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'content']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title', 'content']


admin.site.register(Article, ArticleAdmin)
