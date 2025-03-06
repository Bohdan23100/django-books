from django.shortcuts import render
from .models import Category,Book


def main(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request,'main/main.html',
            {'categories':categories,'books':books})


def profile(request):
    return render(request, 'main/profile.html')

def category_books(request):
    if request.method == 'POST':
        selected_categories = request.POST.getlist('genre[]')
        checked_categories = Category.objects.filter(id__in=selected_categories)
        # print(checked_categories)
        for category in checked_categories:
            category.checked = True



        books = Book.objects.filter(category__id__in=selected_categories)
        categories = Category.objects.all()
        return render(request, 'main/main.html',
                      {'categories': categories, 'books': books,'checked_categories':[category.id for category in checked_categories]})

    return main(request)



