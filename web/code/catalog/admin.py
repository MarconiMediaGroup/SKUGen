from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *

class BrandInline(admin.TabularInline):
    model = Brand
    extra = 1

class VendorInline(admin.TabularInline):
    model = Vendor
    extra = 1

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 15

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class VariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'name','get_numproduct' )
    inlines = (ProductInline, )

class VendorAdmin(admin.ModelAdmin):
    list_display = ('code','name','country',)
    inlines = ( ProductInline, )

class CategoryAdmin(DraggableMPTTAdmin):
    list_display=(
        'tree_actions',
        'indented_title',
        'get_numproduct',
    )
    list_display_links=(
        'indented_title',
    )
    inlines = (ProductInline, CategoryInline, )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'get_sku', 'get_numvariants',
    )
    list_filter = (
        ('category', admin.RelatedOnlyFieldListFilter),
        ('vendor', admin.RelatedOnlyFieldListFilter),
        ('brand', admin.RelatedOnlyFieldListFilter),
    )
    inlines = (VariantInline, )


admin.site.register(Brand, BrandAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
