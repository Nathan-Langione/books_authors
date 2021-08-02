from django.shortcuts import render, redirect
from .models import Books, Authors

# Create your views here.

def index(request):
    context = {
        "all_books": Books.objects.all()    
    }
    return render(request,'index.html', context)

def authors(request):
    context = {
        "all_authors": Authors.objects.all()    
    }
    return render(request,'authors.html', context)

def create_book(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_book = Books.objects.create(title=title,description=description)
        new_book.save()
    return redirect("/")

def create_author(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        new_author = Authors.objects.create(first_name=first_name,last_name=last_name,notes=notes)
        new_author.save()
    return redirect("/authors")

def show_book(request, id):
    context = {
        "book": Books.objects.get(id=id),    
        "authors": Authors.objects.all()
    }
    return render(request,'show_book.html', context)

def show_author(request, id):
    context = {
        "author": Authors.objects.get(id=id),    
        "books": Books.objects.all()
    }
    return render(request,'show_author.html', context)

def add_author(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        author_id = request.POST.get('author_id')
        book_id = request.POST.get('book_id')
        book = Books.objects.get(id=book_id)
        author = Authors.objects.get(id=author_id)
        author.books.add(book)
        #this is not working even though the commands work in the shell and i seem to be passing the right values
    return redirect("/")

def add_book(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        book_id = request.POST.get('book_id')
        author_id = request.POST.get('author_id')
        author = Authors.objects.get(id=author_id)
        book = Books.objects.get(id=book_id)
        book.author.add(author)
        #this is not working even though the commands work in the shell and i seem to be passing the right values
    return redirect("authors")