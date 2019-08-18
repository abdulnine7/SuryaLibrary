from django import forms
from .models import Review

class OrderBookForm(forms.Form):
    book_id = forms.IntegerField(label='Book ID')

class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['book', 'rating', 'description']
