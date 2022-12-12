from flask import render_template, request, redirect
from app import app
from models.book_list import *
from models.book import Book

@app.route('/lofb')
def index():
    return render_template("index.html", title="The Library of Fantastic Books", books=books)

@app.route('/books/<index>')
def one_book(index):
    chosen_book = books[int(index)]
    return render_template("single_book.html", book=chosen_book)

@app.route ('/lofb', methods=['POST'])
def add_book():       #why does this not work when I pass in the parameter of new_book here?
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    blurb = request.form["blurb"]
    checked_out = request.form["checked_out"]
    new_book = Book(title, author, genre, blurb, checked_out)
    books.append(new_book)
    return redirect('/lofb')

@app.route('/lofb/delete/<index>', methods=['POST'])
def delete_book(index):
    books.pop(int(index))
    return redirect('/lofb')
