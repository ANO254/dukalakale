# 🔐 Django Admin Access Guide

## Admin Panel URLs

| Feature             | URL                          |
| ------------------- | ---------------------------- |
| **Admin Dashboard** | `/admin/`                    |
| **Blog Posts**      | `/admin/store/blogpost/`     |
| **Gallery Images**  | `/admin/store/galleryimage/` |
| **Categories**      | `/admin/store/category/`     |
| **Products**        | `/admin/store/product/`      |
| **Orders**          | `/admin/store/order/`        |
| **Users**           | `/admin/auth/user/`          |

---

## How to Access

### Local Development

```
1. Start server: python manage.py runserver
2. Visit: http://localhost:8000/admin/
3. Login with superuser credentials
```

### Production

```
1. Visit: https://yourdomain.com/admin/
2. Login with superuser credentials
```

---

## Superuser Setup (if needed)

```bash
python manage.py createsuperuser
```

Follow prompts:

- Username: admin
- Email: your@email.com
- Password: (secure password)

---

## Login

1. Go to `/admin/`
2. Enter username & password
3. Click "Sign in"
4. You'll see the Django admin dashboard

---

## Navigation to Blog/Gallery Management

From admin dashboard:

### Blog Posts

```
Store → Blog Posts → [Add Blog Post or Edit]
```

### Gallery Images

```
Store → Gallery Images → [Add Gallery Image or Edit]
```

---

## Blog Post Admin Interface

### Fields to Fill

- **Title** - Post headline
- **Author** - Author name
- **Category** - Choose: Design, Business, Technology, Photography, Sustainability, Lifestyle, Other
- **Image** - Upload featured image
- **Excerpt** - Short summary (max 500 chars)
- **Content** - Full article text
- **Published** - Checkbox to show/hide from website

### List View Features

- Search by title or author
- Filter by category, published status
- Quick edit published status (no need to open full form)
- Bulk delete multiple posts
- See image thumbnails

---

## Gallery Image Admin Interface

### Fields to Fill

- **Title** - Image name
- **Category** - Choose: Nature, Landscape, City, Adventure, Beach, Sky, Water, Other
- **Image** - Upload square image (500x500px recommended)
- **Featured** - Checkbox to highlight in gallery

### List View Features

- Search by title
- Filter by category, featured status
- Quick edit featured status
- Bulk delete multiple images
- See image thumbnails

---

## Screenshot Examples

### Adding a Blog Post

```
1. Click "Add Blog Post" button
2. Fill form with your content
3. Upload featured image
4. Check "Published" box
5. Click "Save"
6. Post appears at /blog/ immediately
```

### Adding a Gallery Image

```
1. Click "Add Gallery Image" button
2. Enter image title
3. Select category
4. Upload square image
5. Optionally check "Featured"
6. Click "Save"
7. Image appears at /gallery/ immediately
```

---

## Live Preview

After saving:

| Content Type | View URL    |
| ------------ | ----------- |
| Blog Posts   | `/blog/`    |
| Gallery      | `/gallery/` |
| Full Site    | `/`         |

Your content appears automatically without needing page refresh!

---

## Common Tasks

### Edit a Blog Post

1. `/admin/store/blogpost/`
2. Click post title
3. Modify fields
4. Click "Save"

### Delete a Blog Post

1. `/admin/store/blogpost/`
2. Check checkbox next to post
3. Select "Delete selected blog posts"
4. Click "Go"
5. Confirm deletion

### Hide a Post Without Deleting

1. `/admin/store/blogpost/`
2. Click post to edit
3. **Uncheck** "Published"
4. Click "Save"
   (Post saved as draft, not visible on website)

### Mark Gallery Image as Featured

1. `/admin/store/galleryimage/`
2. Check "Featured" checkbox without opening full form
3. Or click image to edit and check featured
4. Save

---

## Tips

✅ **Always upload images** - Required field
✅ **Fill all required fields** - Marked with asterisk
✅ **Use consistent categories** - Makes filtering easier
✅ **Check spelling** - Appears exactly as typed
✅ **Preview before publishing** - Visit `/blog/` or `/gallery/`
✅ **Use "Published" toggle** - For drafts instead of deleting
✅ **Upload square images** - Gallery works best with 500x500px
✅ **Blog images** - 500x300px recommended for best appearance

---

## Permissions

Your admin user has:

- ✅ Full access to Blog Posts
- ✅ Full access to Gallery Images
- ✅ Full access to all Store data
- ✅ User management

---

## Security Notes

- Keep username/password private
- Don't share admin URL publicly
- Use strong passwords
- Change default admin path in production (optional, advanced)

---

**You're all set! Visit `/admin/` to start managing your blog and gallery!**
