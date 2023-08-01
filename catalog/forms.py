from django import forms
from .models import Book, Author

# Form to create an author.
class AuthorForm(forms.ModelForm):
    pass

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'photo', 'books', ]

# Form to create a book.
class BookForm(forms.ModelForm):
    pass

    class Meta:
        model = Book
        fields = ['image', 'title', 'body', 'authors', ]

