from django.contrib import admin
from product.models import Item, Order, OrderItem, Tax, Discount


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'currency'
    )
    search_fields = ('name',)
    list_filter = ('currency',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'get_items_list',
        'created_at',
    )
    search_fields = ('items__name',)
    list_filter = ('created_at',)

    def get_items_list(self, obj):
        return ", ".join([item.name for item in obj.items.all()])

    get_items_list.short_description = 'Items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'item',
        'quantity'
    )
    search_fields = ('order__id', 'item__name',)
    list_filter = ('order', 'item')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'amount',
    )
    search_fields = ('order__id', 'amount',)
    list_filter = ('order', 'amount')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'amount',
    )
    search_fields = ('order__id',)
    list_filter = ('order', 'amount')
