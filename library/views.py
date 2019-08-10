from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Book

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'library/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book

def about(request):
    return render(request, 'library/about.html', {'title': 'About'})
