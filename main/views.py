from django.shortcuts import render
from .models import Category,Book


def main(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request,'main/main.html',
            {'categories':categories,'books':books})


def profile(request):
    return render(request, 'main/profile.html')








