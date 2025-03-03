from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:book_id>/', views.book, name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
