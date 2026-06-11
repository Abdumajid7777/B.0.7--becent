from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Product
# Register your models here.


# class StudentAdminInline()


class ProductAdmin(admin.ModelAdmin):
    list_display = ( "name", "price", "get_avatar")
    list_filter = ("price",)
    list_per_page = 3
    

    @admin.display(description=_("Аватарка"))
    def get_avatar(self, product):
        if product.avatar:
            return mark_safe(
                f'<img src="{product.avatar.url}" alt="{product.name}" width="100px" />'
            )
        return '_'

admin.site.register(Product, ProductAdmin)