from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# =========================
# Category Model
# =========================
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# =========================
# Product Model
# =========================
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# =========================
# Product Image Model (for lightbox gallery)
# =========================
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.product.name} - Image"


# =========================
# Blog Post Model
# =========================
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Design', 'Design'),
        ('Business', 'Business'),
        ('Technology', 'Technology'),
        ('Photography', 'Photography'),
        ('Sustainability', 'Sustainability'),
        ('Lifestyle', 'Lifestyle'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    excerpt = models.TextField(max_length=500, default='')
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    author = models.CharField(max_length=100, default='Admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# =========================
# Gallery Image Model
# =========================
class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('Nature', 'Nature'),
        ('Landscape', 'Landscape'),
        ('City', 'City'),
        ('Adventure', 'Adventure'),
        ('Beach', 'Beach'),
        ('Sky', 'Sky'),
        ('Water', 'Water'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


# =========================
# Order & OrderItem Models
# =========================
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Paid', 'Paid'),
    ('Canceled', 'Canceled'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def calculate_total(self):
        """Calculate total price based on all order items."""
        total = sum(item.price * item.quantity for item in self.items.all())
        self.total_price = total
        self.save()
        return self.total_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def save(self, *args, **kwargs):
        # Ensure price is synced with product price
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)
        # Update the order total automatically
        self.order.calculate_total()


# =========================
# Investment Model
# =========================
class Investment(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KES {self.amount}"


# =========================
# Subscription Model
# =========================
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email
