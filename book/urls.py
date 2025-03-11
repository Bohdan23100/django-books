from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:book_id>/', views.book, name='book'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_items_plus/<int:item_id>/', views.cart_items_plus, name='cart_items_plus'),  # Назва змінена для узгодженості
    path('cart_items_minus/<int:item_id>/', views.cart_items_minus, name='cart_items_minus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)