from django.urls import path
from .views import (AuthorDeleteView, AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView,
                    BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, add_author_to_book,
                    add_book_to_author)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('<int:book_id>/add_author/<int:author_id>/', add_author_to_book, name='add_author_to_book'),
    path('authors/<int:author_id>/add_book/<int:book_id>/', add_book_to_author, name='add_book_to_author'),

]
