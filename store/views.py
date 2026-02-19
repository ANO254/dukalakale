from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product, BlogPost, GalleryImage, Subscription
from .cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import json
from datetime import datetime

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
# Blog Detail Page
# =========================
def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    # Get related posts (same category, excluding current)
    related_posts = BlogPost.objects.filter(category=post.category).exclude(id=post.id)[:3]
    return render(request, "blog_detail.html", {
        "post": post,
        "related_posts": related_posts
    })

# =========================
# Gallery Page
# =========================
def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, "gallery.html", {"images": images})

# =========================
# Subscribe to Newsletter
# =========================
@require_http_methods(["POST"])
def subscribe(request):
    email = request.POST.get('email', '').strip()
    
    if not email:
        return JsonResponse({'success': False, 'message': 'Email is required'})
    
    # Check if email already exists
    if Subscription.objects.filter(email=email).exists():
        return JsonResponse({'success': False, 'message': 'This email is already subscribed'})
    
    # Save to database
    try:
        Subscription.objects.create(email=email)
        return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Error subscribing. Please try again.'})




def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject="Website Contact",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["tailoonarnold@gmail.com"],
        )

    return render(request, "contact.html")


# =========================
# Checkout / Payment
# =========================
def checkout(request):
    """Handle M-Pesa style checkout"""
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', '').strip()
        amount = request.POST.get('amount', '')
        
        # Get cart items
        cart = Cart(request)
        cart_items = []
        for product_id, item in cart.cart.items():
            try:
                product = Product.objects.get(id=product_id)
                cart_items.append({
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "quantity": item["quantity"],
                    "image": product.image.url if product.image else "",
                })
            except Product.DoesNotExist:
                continue
        
        # Validation
        if not phone_number or not amount:
            messages.error(request, 'Phone number and amount are required')
            return redirect('cart')
        
        if not phone_number.startswith('+254') or len(phone_number) != 13:
            messages.error(request, 'Invalid phone number format')
            return redirect('cart')
        
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                messages.error(request, 'Invalid amount')
                return redirect('cart')
        except ValueError:
            messages.error(request, 'Invalid amount format')
            return redirect('cart')
        
        # Simulate M-Pesa payment processing
        # In production, integrate with Safaricom M-Pesa API
        payment_data = {
            'phone_number': phone_number,
            'amount': amount_float,
            'cart_items': cart_items,
            'timestamp': datetime.now().isoformat(),
            'transaction_id': f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}",
        }
        
        # Send confirmation email
        try:
            order_summary = "\n".join([
                f"- {item['name']} (x{item['quantity']}): KES {item['price'] * item['quantity']:.2f}"
                for item in cart_items
            ])
            
            email_message = f"""
Dear Customer,

Thank you for your order!

📋 ORDER DETAILS:
{order_summary}

💰 TOTAL AMOUNT: KES {amount_float:.2f}
📱 PHONE: {phone_number}
🔐 TRANSACTION ID: {payment_data['transaction_id']}

You will receive an M-Pesa prompt on your phone to complete the payment.

Thank you for supporting DukaLaKale and Kenya's artisans!

Best regards,
DukaLaKale Team
            """
            
            send_mail(
                subject=f"Payment Confirmation - Order {payment_data['transaction_id']}",
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email if request.user.is_authenticated else "customer@dukalakale.com"],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email sending error: {e}")
        
        # Clear cart after successful checkout
        cart.cart.clear()
        request.session['cart'] = {}
        
        # Render success page
        messages.success(request, f'Payment initiated! Check your phone for M-Pesa prompt.')
        return render(request, 'checkout_success.html', {
            'transaction_id': payment_data['transaction_id'],
            'phone_number': phone_number,
            'amount': amount_float,
            'cart_items': cart_items,
        })
    
    return redirect('cart')
