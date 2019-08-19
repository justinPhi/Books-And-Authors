from django.shortcuts import render, HttpResponse, redirect
from .models import *

#page where you add books and can see a table of the books
def index(request):
    context = {
        "allBooks" : Books.objects.all(),
    }
    return render(request, "booksAuthorsApp/index.html", context)

#function thqat creates a new instance of a book
def addBook(request):
    #this is where if validations pass would be
    Books.objects.create(booksTitle = request.POST['addBookTitle'], booksDescription = request.POST['addBookDescription'])
    return redirect("/")

#new html page that shows the book selected via View on HTML page
def showBook(request, val):
    context = {
            'book' : Books.objects.get(id=val)
            }
    return render(request, 'booksAuthorsApp/book.html', context)

# from select, chose an author that is not already related
def addAuthorToBook(request):
    pass
