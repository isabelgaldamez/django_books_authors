from django.shortcuts import render, redirect, HttpResponse
from .models import Books, Authors

# Create your views here.
def index(request):
    context = { 
        "all_books": Books.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def add_book(request):
    if request.method == "POST":
        book_title = request.POST['title']
        book_description = request.POST['description']
        Books.objects.create(title = book_title, desc = book_description)
    return redirect('/')

def book_info(request, book_id):
    book = Books.objects.get(id=book_id)
    context = { 
        "book_info": book,
        "publisher" : book.publishers.all(),
        'authors_list': Authors.objects.all()
    }
    return render(request, 'books_authors_app/books.html', context)

def assign_author(request):
    if request.method == "POST":
        book_id = request.POST['book_id']
        assigned_author = request.POST['author_selection']
        name = assigned_author.split()
    
    
    # Update existing book
    #retrieve the author
    this_author = Authors.objects.get(first_name = name[0])
    # retrieve the boo
    book_add_author = Books.objects.get(id=book_id)
    # add the book to the author
    this_author.books.add(book_id)
    return redirect(f'/books/{book_id}')