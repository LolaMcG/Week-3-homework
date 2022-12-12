import unittest
from models.book import Book
from models.book_list import *

class TestBook(unittest.TestCase):
    def setUp(self):
        self.instance_of_book = book1

    def test_book_has_title(self):
        book_title = self.instance_of_book.title
        self.assertEqual("The Wind-Up Bird Chronicle", book_title)

    def test_book_has_author(self):
        book_author = self.instance_of_book.author
        self.assertEqual("Haruki Murakami", book_author)

    def test_book_has_genre(self):
        book_genre = self.instance_of_book.genre
        self.assertEqual("Magical Realism", book_genre)