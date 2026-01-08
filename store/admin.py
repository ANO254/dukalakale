from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils.html import format_html
from .models import Category, Product, Order, OrderItem, Investment, BlogPost, GalleryImage

User = get_user_model()

# =========================
# Investment Admin
# =========================
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'created_at', 'total_investments')

    def total_investments(self, obj):
        total = Investment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        return f"KES {total}"
    total_investments.short_description = "Total Investment"


# =========================
# Category Admin
# =========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# =========================
# BlogPost and GalleryImage Admin
# =========================
admin.site.register(BlogPost)
admin.site.register(GalleryImage)


# =========================
# Order / OrderItem Admin
# =========================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'customer_email',
        'customer_name',
        'status',
        'total_price',
        'item_count',
        'created_at'
    )
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline]
    actions = ['mark_as_paid', 'mark_as_pending', 'mark_as_canceled']

    def item_count(self, obj):
        """Show total number of items in each order"""
        return obj.items.aggregate(total=Sum('quantity'))['total'] or 0
    item_count.short_description = "Items"

    # Customer details
    def customer_email(self, obj):
        return obj.user.email
    customer_email.short_description = "Customer Email"

    def customer_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip()
    customer_name.short_description = "Customer Name"

    # Bulk actions
    def mark_as_paid(self, request, queryset):
        queryset.update(status='Paid')
    mark_as_paid.short_description = "Mark selected orders as Paid"

    def mark_as_pending(self, request, queryset):
        queryset.update(status='Pending')
    mark_as_pending.short_description = "Mark selected orders as Pending"

    def mark_as_canceled(self, request, queryset):
        queryset.update(status='Canceled')
    mark_as_canceled.short_description = "Mark selected orders as Canceled"


# =========================
# Product Admin
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'low_stock')
    list_filter = ('available', 'category')
    list_editable = ('price', 'stock')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

    def low_stock(self, obj):
        return obj.stock < 5
    low_stock.boolean = True
    low_stock.short_description = "Low Stock"


# =========================
# User Admin (Staff & Customers)
# =========================
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')


# Unregister default User and register custom
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
