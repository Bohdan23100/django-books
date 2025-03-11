from django.shortcuts import render
from .models import Category,Book


def main(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request,'main/main.html',
            {'categories':categories,'books':books})


def profile(request):
    return render(request, 'user_profile/profile.html')

def category_books(request):
    if request.method == 'POST':
        selected_categories = list(map(int, request.POST.getlist('genre[]')))
        books = Book.objects.filter(category__id__in=selected_categories)
        categories = Category.objects.all()
        return render(request, 'main/main.html''cart/cart.html',
                      {'categories': categories, 'books': books,'checked_categories':selected_categories})

    return main(request)

def cart(request):
    return render(request, 'cart/cart.html')

