from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile



# List view for Book model
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

def books(request):
    # The function creates a list of all authors of the book.
    book_list = []
    books = Book.objects.all()

    for book in books:
        authors = book.authors.all()
        author_names = [f"{author.first_name} {author.last_name}" for author in authors]
        book_list.append(f"{book.title}: {', '.join(author_names)}")

    return render(request, 'books.html', {'book_list': book_list})

# Create view for Book model
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'


# Update view for Book model
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['image', 'title', 'body', ]

    def form_valid(self, form):
        # Получаем объект книги из базы данных
        book = form.save(commit=False)
        # Получаем загруженное изображение из формы
        image = form.cleaned_data['image']
        # Если загружено изображение, то сохраняем его в файловой системе
        if image:
            file_name = default_storage.save(image.name, ContentFile(image.read()))
            book.image = file_name
        # Сохраняем изменения в базе данных
        book.save()
        return super().form_valid(form)


# Delete view for Book model
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')


# Detail view for Book model
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

def add_author_to_book(request, book_id, author_id):
    book = get_object_or_404(Book, id=book_id)
    author = get_object_or_404(Author, id=author_id)
    book.authors.add(author)
    book.save()
    return redirect('book_detail', pk=book.pk)

# List view for Author model
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


def authors(request):
    # The function creates a list of all books written by this author
    author_list = []
    authors = Author.objects.all()

    for author in authors:
        books = author.books.all()
        book_titles = [book.title for book in books]
        author_list.append(f"{author.first_name} {author.last_name}: {', '.join(book_titles)}")

    return render(request, 'authors.html', {'author_list': author_list})


# Create view for Author  model
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_list')


# Update view for Author model
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_update.html'
    success_url = reverse_lazy('master_list')

    def get_object(self):
        # Get the current author object by its primary key
        return get_object_or_404(Author, pk=self.kwargs['pk'])

    def form_valid_author(self, form):
        author = form.save(commit=False)
        # Save the uploaded photo to the server and set it as the master's photo
        photo = form.cleaned_data['photo']
        if photo:
            file_name = default_storage.save(photo.name, ContentFile(photo.read()))
            author.photo = file_name
        author.save()
        return super().form_valid_author(form)


# Delete view for Author model
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')


# Detail view for Master model
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

def add_book_to_author(request, author_id, book_id):
    book = get_object_or_404(Book, id=book_id)
    author = get_object_or_404(Author, id=author_id)
    author.books.add(book)
    author.save()
    return redirect('author_detail', pk=author.pk)

