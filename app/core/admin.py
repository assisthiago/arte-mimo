from django.contrib import admin

from app.core.models import Background, Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "active")
    list_filter = ("category", "active")
    search_fields = ("name",)
    list_editable = ("active",)


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ("photo", "active")
    list_filter = ("active",)
    list_editable = ("active",)
