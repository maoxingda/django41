from django.contrib import admin

from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    admin_order = 1
    autocomplete_fields = (
        'author',
    )


@admin.register(Author)
class AuthorAmdin(admin.ModelAdmin):
    admin_order = 21
    search_fields = (
        'name',
    )
