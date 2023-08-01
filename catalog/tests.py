from django.test import TestCase

from django.urls import reverse, resolve
from .models import Book, Author
from .views import BookListView, AuthorListView


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test author
        cls.author1 = Author.objects.create(first_name='Ivan', last_name='Ivanov')
        cls.author2 = Author.objects.create(first_name='John', last_name='Doe')

        cls.book1 = Book.objects.create(title='New Book 1', body='This is a very interesting book')
        cls.book1.authors.add(cls.author1, cls.author2)

        cls.book2 = Book.objects.create(title='New Book 2', body='This is another interesting book')
        cls.book2.authors.add(cls.author2)


    def test_book_model(self):
        """
        Test for checking Book model attributes
        """
        self.assertEqual(self.book1.title, "New Book 1")
        self.assertEqual(self.book1.body, "This is a very interesting book")
        self.assertEqual(self.book1.authors.count(), 2)
        self.assertIn(self.author1, self.book1.authors.all())
        self.assertIn(self.author2, self.book1.authors.all())
        self.assertEqual(str(self.book1), "New Book 1")
        self.assertEqual(self.book1.get_absolute_url(), "/catalog/1")



    def test_book_listview(self):
        """
        Test for checking book list view page rendering
        """
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Book')
        self.assertTemplateUsed(response, 'book_list.html')

    def test_list_url_resolve_view(self):
        view = resolve(reverse('book_list'))
        self.assertEqual(view.func.view_class, BookListView)

    def test_view_displays_authors(self):
        """
        Test for checking if the view displays the correct authors for each book
        """
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'Ivan Ivanov')
        self.assertContains(response, 'New Book 1')