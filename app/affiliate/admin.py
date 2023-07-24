from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import ProductCat ,Product_sub_cat,Brand, Product,Blog,GenderType,Color, Comment


admin.site.register(ProductCat)
admin.site.register(Product_sub_cat)

class ProductModel(SummernoteModelAdmin):
    summernote_fields = ('product_short_description','product_long_description')
    
class BlogModel(SummernoteModelAdmin):
    summernote_fields = ('blog_body','blog_short_description')

admin.site.register(Product, ProductModel)
admin.site.register(Blog, BlogModel)
admin.site.register(Brand)
admin.site.register(GenderType)
admin.site.register(Color)
admin.site.register(Comment)
