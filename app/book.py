from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Book
from app.forms import AddBook, UpdateBook

books = Blueprint('books', __name__, url_prefix='/books')


@books.route('/list', methods=['GET'])
def render_books_list():
    books_list = Book.query.all()
    return render_template('book/books_list.html', books_list=books_list)


@books.route('/add', methods=['GET'])
def render_add_book():
    form = AddBook()
    return render_template('book/add_book.html', form=form)


@books.route('/add', methods=['POST'])
def add_book_to_db():
    form = AddBook()
    if request.method == 'POST':
        if form.validate_on_submit():
            book = Book(
                title=request.form.get('title'),
                genre=request.form.get('genre')
            )
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('books.render_books_list'))


@books.route('/update/<int:book_id>', methods=['GET'])
def render_update_book(book_id: int):
    book = Book.query.get(book_id)
    form = UpdateBook(data={
        'title': book.title,
        'genre': book.genre
    })
    return render_template('/book/update_book.html', form=form, book_id=book_id)


@books.route('/update/<int:book_id>', methods=['POST'])
def update_book_to_db(book_id: int):
    form = UpdateBook()
    if request.method == 'POST':
        if form.validate_on_submit():
            book = Book.query.get(book_id)
            book.title = request.form.get('title')
            book.genre = request.form.get('genre')
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('books.render_books_list'))
