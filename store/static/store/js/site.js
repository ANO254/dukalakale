function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.add-to-cart-btn');
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      e.preventDefault();
      const productId = this.dataset.productId;
      const url = `/add-to-cart/${productId}/`;
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({})
      })
      .then(r => r.json())
      .then(data => {
        if (data.success) {
          // simple visual feedback: update cart badge if present
          const badge = document.querySelector('.nav-cart-badge');
          if (badge) badge.textContent = data.cart_count;
          // small toast / alert
          const el = document.createElement('div');
          el.className = 'toast align-items-center text-bg-dark border-0';
          el.setAttribute('role','alert');
          el.setAttribute('aria-live','assertive');
          el.setAttribute('aria-atomic','true');
          el.style.position='fixed'; el.style.top='1rem'; el.style.right='1rem';
          el.style.zIndex = 9999;
          el.innerHTML = `<div class="d-flex"><div class="toast-body">Added to cart</div><button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button></div>`;
          document.body.appendChild(el);
          const toast = new bootstrap.Toast(el);
          toast.show();
          setTimeout(()=>{toast.hide(); el.remove();}, 2500);
        }
      }).catch(()=>{
        alert('Could not add to cart.');
      });
    });
  });
});
