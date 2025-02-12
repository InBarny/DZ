from django.contrib import admin

# Register your models here.
from .models import Category, Post, Like, Coment, Donat


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Coment)
class Comment(admin.ModelAdmin):
    ...

@admin.register(Like)
class Reaction(admin.ModelAdmin):
    ...

@admin.register(Donat)
class Comment(admin.ModelAdmin):
    ...