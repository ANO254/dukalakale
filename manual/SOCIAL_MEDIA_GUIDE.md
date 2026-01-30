# Social Media Icons & Media Linking Guide

## ✅ What We've Done

### 1. **Added Bootstrap Icons CDN**
   - Added to `base.html` - All templates now have access to 2000+ icons
   - Icons used: Facebook, Instagram, Twitter, TikTok, YouTube, LinkedIn

### 2. **Updated Contact Page Icons**
   - Replaced emoji icons with proper Bootstrap Icons
   - Added hover effect (scales up + color change on hover)
   - Updated social links with real URLs (update with your actual profiles)

### 3. **Icon Classes Used**
   ```
   bi-facebook      → Facebook
   bi-instagram     → Instagram
   bi-twitter-x     → Twitter/X
   bi-tiktok        → TikTok
   bi-youtube       → YouTube
   bi-linkedin      → LinkedIn
   bi-geo-alt-fill  → Location
   bi-envelope-fill → Email
   bi-telephone-fill → Phone
   ```

---

## 📱 How to Add Social Icons Anywhere

### Basic Example:
```html
<a href="https://instagram.com/yourprofile" target="_blank" class="hover-icon">
  <i class="bi bi-instagram"></i>
</a>
```

### With Styling:
```html
<a href="https://facebook.com/yourpage" target="_blank" class="text-dark text-decoration-none hover-icon" title="Follow us on Facebook">
  <i class="bi bi-facebook fs-5"></i>
</a>
```

### Icon Size Classes:
```
fs-1 → Extra large (2rem)
fs-2 → Large (1.75rem)
fs-3 → Medium (1.5rem)
fs-4 → Default (1.25rem)
fs-5 → Small (1rem)
fs-6 → Extra small (0.875rem)
```

---

## 📁 How to Link with Media Files (Django)

### 1. **In Your Django Settings** (`duka/settings.py`):
```python
# Media files configuration
MEDIA_URL = '/media/'  # URL path to access media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Folder where files are stored
```

### 2. **In Your Django URLs** (`duka/urls.py`):
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your other paths ...
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. **Using Media in Templates**:

#### Example 1: Product Images
```html
<!-- In your template -->
<img src="{{ product.image.url }}" alt="{{ product.name }}">
<!-- Renders as: <img src="/media/products/image.jpg" alt="Product Name"> -->
```

#### Example 2: Blog Post Featured Image
```html
<img src="{{ post.featured_image.url }}" alt="{{ post.title }}" class="img-fluid">
```

#### Example 3: Gallery Images
```html
{% for gallery_image in gallery_images %}
  <img src="{{ gallery_image.image.url }}" alt="{{ gallery_image.title }}">
{% endfor %}
```

### 4. **Uploading Files Through Django Admin**:
- Go to `/admin/`
- When you create a Product, BlogPost, or any model with an ImageField:
  - Click the upload button next to the image field
  - Select image from your computer
  - Django automatically stores it in `/media/` folder
  - The `.url` property gives you the web path

### 5. **Directory Structure**:
```
dukalakale/
├── media/
│   ├── blog_images/      ← Blog post images
│   ├── gallery_images/   ← Gallery images
│   ├── products/         ← Product images
│   └── uploads/          ← Other uploads
├── store/
├── duka/
└── manage.py
```

---

## 🎨 Using Media with Social Links

### Example: Social Media Links with Images
```html
<!-- Social Links with Icons -->
<div class="d-flex gap-3">
  <a href="https://facebook.com/dukalakale" target="_blank">
    <i class="bi bi-facebook fs-4 text-primary hover-icon"></i>
  </a>
  
  <!-- Or with image logo -->
  <a href="https://instagram.com/dukalakale" target="_blank">
    <img src="{{ MEDIA_URL }}social_logos/instagram.png" alt="Instagram" style="width: 30px; height: 30px;">
  </a>
</div>
```

### Store Social Image Files:
```
media/
├── social_logos/
│   ├── facebook.png
│   ├── instagram.png
│   ├── twitter.png
│   └── tiktok.png
```

### Access in Template:
```html
<img src="/media/social_logos/instagram.png" alt="Instagram" style="width: 30px;">
```

---

## 🔗 Current Social Media Links (Update These)

Update these URLs in `contact.html` with your actual profiles:

```
Facebook:  https://facebook.com/dukalakale
Instagram: https://www.instagram.com/duka.la.kale
Twitter:   https://twitter.com/dukalakale
TikTok:    https://www.tiktok.com/@dukalakale
YouTube:   https://www.youtube.com/@dukalakale
LinkedIn:  https://www.linkedin.com/company/dukalakale
```

---

## 🌐 Available Bootstrap Icons

Common social media icons:
- `bi-facebook` - Facebook
- `bi-instagram` - Instagram
- `bi-twitter-x` - Twitter/X
- `bi-tiktok` - TikTok
- `bi-youtube` - YouTube
- `bi-linkedin` - LinkedIn
- `bi-github` - GitHub
- `bi-discord` - Discord
- `bi-twitch` - Twitch
- `bi-pinterest` - Pinterest
- `bi-reddit` - Reddit
- `bi-telegram` - Telegram
- `bi-whatsapp` - WhatsApp

**Full list**: https://icons.getbootstrap.com/

---

## ⚡ Quick Reference

### Add Icon with Hover Effect:
```html
<a href="#" class="hover-icon text-dark text-decoration-none">
  <i class="bi bi-instagram fs-4"></i>
</a>
```

### Add Image with Responsive Size:
```html
<img src="{{ product.image.url }}" alt="{{ product.name }}" class="img-fluid">
```

### Add Social Icon Row:
```html
<div class="d-flex gap-3">
  {% comment %} Facebook {% endcomment %}
  <a href="https://facebook.com/yourpage" target="_blank" class="hover-icon">
    <i class="bi bi-facebook fs-4"></i>
  </a>
  {% comment %} Instagram {% endcomment %}
  <a href="https://instagram.com/yourprofile" target="_blank" class="hover-icon">
    <i class="bi bi-instagram fs-4"></i>
  </a>
</div>
```

---

## ✅ Implementation Status

- ✅ Bootstrap Icons CDN added to base.html
- ✅ Contact page updated with proper icons
- ✅ Hover effects added (scale + color change)
- ✅ Social media links configured
- ✅ Media configuration explained

All files are linked and working! The hover effect will trigger when you move your mouse over any social icon.
