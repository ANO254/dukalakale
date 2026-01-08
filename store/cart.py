from decimal import Decimal
from .models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.session['cart'] = self.cart

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session['cart'] = self.cart

    def items(self):
        return self.cart

    def total(self):
        total_price = Decimal('0.00')
        for item_id, item_data in self.cart.items():
            try:
                product = Product.objects.get(id=item_id)
                total_price += product.price * item_data['quantity']
            except Product.DoesNotExist:
                continue
        return total_price

    def total_ksh(self):
        return f"KES {self.total():.2f}"
