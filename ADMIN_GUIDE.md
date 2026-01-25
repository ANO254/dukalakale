# Admin Guide - Blog & Gallery Management

## Overview

Your blog and gallery are now fully integrated with Django Admin. You can easily manage all posts and images from the admin dashboard at `/admin/`.

---

## 🎯 Blog Post Management

### How to Add a Blog Post

1. Go to **Django Admin** → **Store** → **Blog Posts**
2. Click **"Add Blog Post"** button
3. Fill in the following fields:

| Field         | Description                    | Example                                                                     |
| ------------- | ------------------------------ | --------------------------------------------------------------------------- |
| **Title**     | Post headline                  | "Top 10 E-commerce Trends for 2026"                                         |
| **Author**    | Author name                    | "Sarah Johnson"                                                             |
| **Category**  | Post category                  | Design, Business, Technology, Photography, Sustainability, Lifestyle, Other |
| **Image**     | Featured image                 | Upload a JPG/PNG (recommended: 500x300px)                                   |
| **Excerpt**   | Short summary (max 500 chars)  | Brief description shown on blog listing                                     |
| **Content**   | Full post content              | Main article text (supports HTML)                                           |
| **Published** | Enable/disable post visibility | Check to make visible on website                                            |

4. Click **"Save"** to publish

### Edit Existing Posts

1. Go to **Blog Posts** list
2. Click on the post title to edit
3. Make your changes
4. Click **"Save"**

### Delete a Post

1. Select the post(s) from the list
2. Choose "Delete selected blog posts" from the dropdown
3. Confirm deletion

---

## 🖼️ Gallery Management

### How to Add Gallery Images

1. Go to **Django Admin** → **Store** → **Gallery Images**
2. Click **"Add Gallery Image"** button
3. Fill in the following fields:

| Field        | Description      | Example                                                      |
| ------------ | ---------------- | ------------------------------------------------------------ |
| **Title**    | Image name/title | "Summer Waves"                                               |
| **Category** | Image category   | Nature, Landscape, City, Adventure, Beach, Sky, Water, Other |
| **Image**    | Photo file       | Upload JPG/PNG (recommended: square 500x500px)               |
| **Featured** | Mark as featured | Check to highlight in gallery                                |

4. Click **"Save"** to add to gallery

### Organize Gallery

- **Featured images** appear first in the gallery
- Images are sorted by upload date (newest first)
- Click the image thumbnail in admin to preview before saving

---

## 📱 How It Works

### Blog Page (`/blog/`)

- Displays all **published** blog posts in a 3-column responsive grid
- Shows: Image, Category badge, Date, Title, Excerpt, "Read More" button
- Post metadata (author, date) from admin fields
- Cards have smooth hover animations

### Gallery Page (`/gallery/`)

- Displays all gallery images in a 3x3 grid (responsive: 2 columns on tablet, 1 on mobile)
- Click any image to open **lightbox modal** with:
  - Full-size image view
  - Navigation buttons (Previous/Next)
  - Keyboard shortcuts (Arrow keys, ESC)
  - Image counter (e.g., "3 / 12")
  - Close button

---

## 🔧 Tips & Tricks

### For Blog Posts

- **Keep excerpts short** - They preview on the listing page
- **Use categories consistently** - Helps with future filtering features
- **Images work best** when 500x300px (aspect ratio 16:9)
- **Unpublish posts** by unchecking "Published" instead of deleting
- **Draft posts** - Uncheck "Published" to save as draft without showing on site

### For Gallery

- **Use square images** - They display best in the grid (500x500px)
- **Add descriptive titles** - These appear in the lightbox
- **Categories help organize** - Mark related images with same category
- **Featured flag** - Use to highlight important images

---

## 📊 Admin Dashboard Features

### Blog Posts List View

- **Search by**: Title or Author
- **Filter by**: Category, Published status, Date created
- **Quick edit**: Status (Published/Unpublished) without opening full form
- **Bulk actions**: Delete multiple posts at once
- **Image preview**: Thumbnail shows in admin list

### Gallery Images List View

- **Search by**: Title
- **Filter by**: Category, Featured status, Upload date
- **Quick edit**: Featured status without opening full form
- **Bulk actions**: Delete multiple images at once
- **Image preview**: Thumbnail shows in admin list

---

## ✅ Database Fields Reference

### BlogPost Model

```
id (auto)
title (required)
author (required)
category (required)
image (required - ImageField)
excerpt (required - up to 500 chars)
content (required - TextField)
published (default: True)
created_at (auto-set)
updated_at (auto-set)
```

### GalleryImage Model

```
id (auto)
title (required)
category (required)
image (required - ImageField)
featured (default: False)
uploaded_at (auto-set)
```

---

## 🚀 Next Steps

1. **Visit Admin**: http://yoursite.com/admin/
2. **Login** with your superuser credentials
3. **Add a Blog Post** with test content
4. **Add Gallery Images** to test the lightbox
5. **Visit** `/blog/` and `/gallery/` to see your content live!

---

## 🐛 Troubleshooting

### Posts not showing?

- ✓ Check "Published" checkbox is enabled
- ✓ Verify image was uploaded successfully
- ✓ Check browser cache (hard refresh: Ctrl+F5)

### Images not appearing?

- ✓ Ensure MEDIA_ROOT is configured in settings.py
- ✓ Check file permissions on media folder
- ✓ Verify image format (JPG, PNG recommended)

### Images too large/small?

- ✓ Gallery: Recommended 500x500px (square)
- ✓ Blog: Recommended 500x300px (16:9 aspect)

---

**Questions?** Check Django admin documentation or contact your developer.
