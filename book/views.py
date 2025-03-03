from django.shortcuts import render
from main.models import Book


def book(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'book/book.html',{'book':book})