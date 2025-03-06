from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.main,name = 'main'),
    path('category_books/',views.category_books,name = 'category_books'),
] + static(settings.STATIC_URL, dokument_root=settings.STATIC_ROOT)



