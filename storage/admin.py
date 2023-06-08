from django.contrib import admin

from storage.models import Product, Article, Box


# Register your models here.

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Box)
