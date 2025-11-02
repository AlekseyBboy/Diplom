from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'all', 'available' ]
    list_filter = ['genre', 'author']
    search_fields = ['title', 'author__name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']
    search_fields = ['user__first_name', 'user__last_name', 'group']


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['book', 'student', 'bor_date', 'get_date', 'ret_date']
    list_filter = ['bor_date', 'get_date']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


