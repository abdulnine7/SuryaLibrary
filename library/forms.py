from django import forms

class OrderBookForm(forms.Form):
    book_id = forms.IntegerField(label='Book ID')
