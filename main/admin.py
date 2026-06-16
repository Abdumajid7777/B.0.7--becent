from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Product, Category


# Register your models here.


# class ProductAdminInline()


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "price", "description", "color", 
        "category"
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "price", "age", "color")
    list_filter = ("category",)

    @admin.display(description=_("Аватарка"))
    def get_avatar(self, product):
        if product.avatar:
            return mark_safe(
                f'<img src="{product.avatar.url}" alt="{product.name}" width="100px" />'
            )
        return '_'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", )

    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)