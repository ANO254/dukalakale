from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.db.models import Sum

from store.models import Product, Order, OrderItem, Investment

User = get_user_model()


# =========================
# Dashboard Home
# =========================
@staff_member_required
def dashboard_home(request):
    """Display the main admin dashboard with KPIs and charts."""

    # ---- KPIs ----
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(stock__lt=5)

    # ---- Orders by status ----
    orders_by_status = (
        Order.objects
        .values('status')
        .annotate(count=Sum(1))
        .order_by('status')
    )

    # ---- Total Revenue (Confirmed Orders Only) ----
    total_revenue = (
        Order.objects.filter(status='Confirmed')
        .aggregate(total=Sum('total_price'))['total'] or 0
    )

    # ---- Best Sellers ----
    best_sellers = (
        OrderItem.objects
        .values('product__name')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')[:5]
    )

    # ---- Investment & Profit ----
    total_investment = Investment.objects.aggregate(total=Sum('amount'))['total'] or 0
    profit = total_revenue - total_investment

    # ---- Monthly Sales Chart (Confirmed Orders Only) ----
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_sales = []
    for month_number in range(1, 13):
        month_total = (
            Order.objects.filter(
                created_at__month=month_number,
                status='Confirmed'  # Only confirmed orders
            ).aggregate(total=Sum('total_price'))['total'] or 0
        )
        monthly_sales.append(month_total)

    # ---- Pass all data to template ----
    context = {
        'total_orders': total_orders,
        'orders_by_status': orders_by_status,
        'total_revenue': total_revenue,
        'total_products': total_products,
        'low_stock': low_stock,
        'best_sellers': best_sellers,
        'total_investment': total_investment,
        'profit': profit,
        'months': months,
        'monthly_sales': monthly_sales,
    }

    return render(request, 'dashboard/home.html', context)


# =========================
# Orders Page
# =========================
@staff_member_required
def orders_page(request):
    """Display all orders in the dashboard."""
    orders = Order.objects.all()
    return render(request, 'dashboard/orders.html', {'orders': orders})


# =========================
# Products Page
# =========================
@staff_member_required
def products_page(request):
    """Display all products in the dashboard."""
    products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'products': products})


# =========================
# Customers Page
# =========================
@staff_member_required
def customers_page(request):
    """Display all customers and total count."""
    customers = User.objects.all()
    return render(
        request,
        'dashboard/customers.html',
        {
            'customers': customers,
            'total_customers': customers.count(),
        }
    )
