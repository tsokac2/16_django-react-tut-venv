from django.contrib import admin
from .models import Author, Book, BookNumber, Character

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    search_fields = ['title']

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)


