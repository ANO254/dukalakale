from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop_view, name="shop"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/update-quantity/<int:product_id>/", views.update_cart_quantity, name="update_cart_quantity"),
    path("blog/", views.blog_view, name="blog"),
    path("blog/<int:id>/", views.blog_detail, name="blog_detail"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("subscribe/", views.subscribe, name="subscribe"),
]
