from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Book, Author
from app.forms import AddBook, UpdateBook, authors_list_form_builder, select_values_by_key_prefix

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


@books.route('/<int:book_id>/delete', methods=['GET'])
def delete_book_by_id(book_id: int):
    book = Book.query.get(book_id)
    if not book:
        print(f"Książka o numerze id [{book_id}] nie został usunięty. Prownodowobnie nie istnieje.")
        return redirect(url_for('books.render_books_list'))
    else:
        book.authors = []
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('books.render_books_list'))


@books.route('/<int:book_id>/details', methods=['GET'])
def render_book_details(book_id: int):
    book = Book.query.get(book_id)
    return render_template('book/books_list.html', book=book)


@books.route('/<int:book_id>/authors', methods=['GET'])
def render_form_authors_for_book(book_id: int):
    book = Book.query.get(book_id)
    authors = Author.query.all()
    authors_ids = [author.id for author in book.authors]
    form = authors_list_form_builder(authors, authors_ids)
    return render_template('book/attach_author_to_book.html', form=form, book_id=book_id)


@books.route('/<int:book_id>/authors', methods=['POST'])
def update_authors_for_books(book_id: int):
    authors = Author.query.all()
    form = authors_list_form_builder(authors, authors_ids=[])

    if request.method == 'POST':
        if form.validate_on_submit():
            authors_ids = select_values_by_key_prefix(
                key_prefix='auth_',
                dictionary=request.form
            )
            book = Book.query.get(book_id)
            book.authors = []
            for author_id in authors_ids:
                author = Author.query.get(author_id)
                book.authors.append(author)
            db.session.commit()

    return redirect(url_for('books.render_book_details', book_id=book_id))
