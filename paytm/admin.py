
# Register your models here.
from django.contrib import admin
from .models import Paytm_Payment, Paytm_Order, Paytm_OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = Paytm_OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

admin.site.register(Paytm_Payment)
admin.site.register(Paytm_Order, OrderAdmin)
admin.site.register(Paytm_OrderProduct)