from django.contrib import admin

from orders.models import Order, OrderItem


# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment",
        "is_paid",
        "time_created",
    )

    search_fields = (
        "requires_delivery",
        "payment",
        "is_paid",
        "time_created",
    )
    readonly_fields = ("time_created",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment",
        "is_paid",
        "time_created",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("time_created",)
    list_filter = (
        "requires_delivery",
        "status",
        "payment",
        "is_paid",
    )
    inlines = (OrderItemTabulareAdmin,)
