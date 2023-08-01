from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    """Model representing a book that has a cover, a title, and a brief summary"""
    image = models.ImageField(upload_to='images/', default='images/placeholder.png', blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    authors = models.ManyToManyField('Author')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse("book_detail", kwargs={'pk': self.pk})

    def get_authors(self):
        """The function creates a list of all authors of the book."""
        return ', '.join([str(author) for author in self.authors.all()])




class Author(models.Model):
    """Model representing an author. He has a first_name, last_name, photo"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/', default='images/placeholder.png', blank=True)
    books = models.ManyToManyField(Book)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)



