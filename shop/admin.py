from django.contrib import admin
from .models import Menu, Order, Timing


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "inStock", "price")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("profile", "item", "quantity", "order_completed")


class TimingAdmin(admin.ModelAdmin):
    list_display = ("shop_open", "shop_close")


admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Timing, TimingAdmin)
