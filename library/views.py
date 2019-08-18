from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Delivery, Review
from .forms import OrderBookForm, CreateReviewForm

class BookListView(ListView):
    model = Book
    template_name = 'library/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book

    def get_reviews(self):
        book = get_object_or_404(Book, id=self.kwargs.get('pk'))
        return Review.objects.filter(book = book).filter(admin_confirmed=True)

    def get_review_form(self):
        form = CreateReviewForm(initial = {'book': get_object_or_404(Book, id=self.kwargs.get('pk'))})
        form.fields['book'].widget.attrs['hidden'] = True
        form.fields['book'].label = ""
        return form

def about(request):
    return render(request, 'library/about.html', {'title': 'About'})

@login_required
def addReview(request):

    if (request.method == 'POST'):
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            rating = form.cleaned_data['rating']
            description = form.cleaned_data['description']
            user = request.user

            if not user.profile.admin_approved:
                messages.info(request, 'Sorry admin need to aproves your profile to order books and post reviews.')
                return redirect('book-detail', pk=book.id)

            review = Review.objects.create(book=book,user=user,rating=rating,description=description)
            review.save()
            messages.info(request, 'Thank you for your valuble review. It will be visible on site once admin aproves it.')
            return redirect('book-detail', pk=book.id)
        else:
            messages.info(request, 'Something is wrong. Please try again later')
            return redirect('library-home')

@login_required
def orderBook(request):
    if (request.method == 'GET'):
        form = OrderBookForm(request.GET)

        #if user profile is not approved
        if not request.user.profile.admin_approved:
            messages.info(request, 'Your profile need to be approves by admin to order books. Please contact admin.')
            return redirect('library-home')

        #if user area is not set
        if not request.user.profile.area:
            messages.info(request, 'You need to set your area first!')
            return redirect('profile')

        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            #Received booking request with book id now first check if available_copies
            book = get_object_or_404(Book, id = book_id)
            delivery = request.user.profile.area.day

            if book.available_copies > 0: #means available
                context = {
                    'book' : book,
                    'delivery' : delivery
                }
                return render(request, 'library/order_confirm.html', context)

            else: #means not available.
                context = {
                    'book' : book,
                }
                return render(request, 'library/order_unavailable.html', context)

def orderConfirmBook(request):
    if (request.method == 'GET'):
        form = OrderBookForm(request.GET)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            #Add to users notification and delivery shedule list
            delivery = Delivery.objects.create(book = get_object_or_404(Book, id = book_id), user = request.user, area = request.user.profile.area)
            delivery.save()

            messages.success(request, 'Your book has been added to our delivery schedule! We will get it to you soon!')
            return render(request, 'library/home.html')
        else:
            messages.warning(request, 'Something is wrong! Please try again later!')
            return render(request, 'library/home.html')
    else:
        messages.warning(request, 'Something is wrong! Please try again later!')
        return render(request, 'library/home.html')
