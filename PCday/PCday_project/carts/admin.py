from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'time_created'
    search_fields = 'product', 'quantity', 'time_created'
    readonly_fields = ('time_created',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_display', 'quantity', 'time_created', ]
    list_filter = ['user', 'product__name', 'time_created', ]

    def product_display(self, obj):
        return str(obj.product.name)
