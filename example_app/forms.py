from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        