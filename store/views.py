from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, BlogPost, GalleryImage
from .cart import Cart

# =========================
# Home Page
# =========================
def home(request):
    products = Product.objects.filter(available=True)[:6]
    return render(request, "home.html", {"products": products})

# =========================
# Shop Page
# =========================
def shop_view(request):
    products = Product.objects.filter(available=True)
    return render(request, "shop.html", {"products": products})

# =========================
# Product Detail Page
# =========================
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product_detail.html", {"product": product})

# =========================
# Contact Page
# =========================
def contact(request):
    if request.method == "POST":
        # handle form submission here
        pass
    return render(request, "contact.html")

# =========================
# Add to Cart
# =========================
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # AJAX support
    if request.method == 'POST' or request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart.add(product)
        return JsonResponse({
            'success': True,
            'cart_count': sum(item['quantity'] for item in cart.cart.values()),
            'total': f"KES {cart.total():.2f}",
        })

    # Normal request
    cart.add(product)
    return redirect("cart")

# =========================
# View Cart
# =========================
def cart_view(request):
    cart = Cart(request)
    cart_items = []

    for product_id, item in cart.cart.items():
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            continue

        cart_items.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": item["quantity"],
            "image": product.image.url if product.image else "",
        })

    total = sum(item["price"] * item["quantity"] for item in cart_items)

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total,
    })

# =========================
# Remove from Cart
# =========================
def remove_from_cart(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)
    return redirect('cart')

# =========================
# Update Cart Quantity
# =========================
def update_cart_quantity(request, product_id):
    if request.method == 'POST' or request.headers.get('x-requested-with') == 'XMLHttpRequest':
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.add(product, quantity=quantity, update_quantity=True)

        total = cart.total()
        return JsonResponse({
            "success": True,
            "total": f"KES {total:.2f}"
        })
    return JsonResponse({"success": False}, status=400)

# =========================
# Blog Page
# =========================
def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, "blog.html", {"posts": posts})

# =========================
# Gallery Page
# =========================
def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, "gallery.html", {"images": images})
