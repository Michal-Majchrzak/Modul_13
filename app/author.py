from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Author, Book
from app.forms import AddAuthor, books_list_form_builder, select_values_by_key_prefix

authors = Blueprint('authors', __name__, url_prefix='/authors')


@authors.route('/list', methods=['GET'])
def render_authors_list():
    authors_list = Author.query.all()
    return render_template('author/author_list.html', authors_list=authors_list)


@authors.route('/add', methods=['GET'])
def render_add_author():
    form = AddAuthor()
    return render_template('author/add_author.html', form=form)


@authors.route('/add', methods=['POST'])
def add_author_to_db():
    form = AddAuthor()
    if request.method == 'POST':
        if form.validate_on_submit():
            author = Author(
                name=request.form.get('name'),
                lastname=request.form.get('lastname')
            )
            db.session.add(author)
            db.session.commit()

    return redirect(url_for('authors.render_authors_list'))


@authors.route('/update/<int:author_id>', methods=['GET'])
def render_update_author(author_id: int):
    author = Author.query.get(author_id)
    form = AddAuthor(data={
        'name': author.name,
        'lastname': author.lastname
    })
    form.button.label.text = 'Zaktualizuj'
    return render_template('/author/update_author.html', form=form, author_id=author_id)


@authors.route('/update/<int:author_id>', methods=['POST'])
def update_author_to_db(author_id: int):
    form = AddAuthor()
    if request.method == 'POST':
        if form.validate_on_submit():
            author = Author.query.get(author_id)
            author.name = request.form.get('name')
            author.lastname = request.form.get('lastname')
            db.session.add(author)
            db.session.commit()
            return redirect(url_for('authors.render_authors_list'))


@authors.route('/<int:author_id>/details', methods=['GET'])
def render_author_details(author_id: int):
    author = Author.query.get(author_id)
    return render_template('author/author_list.html', author=author)


@authors.route('/<int:author_id>/delete', methods=['GET'])
def delete_author_by_id(author_id: int):
    author = Author.query.get(author_id)
    if not author:
        print(f"Autor o numerze id [{author_id}] nie został usunięty. Prownodowobnie nie istnieje.")
        return redirect(url_for('authors.render_authors_list'))
    else:
        author.books = []
        db.session.delete(author)
        db.session.commit()
    return redirect(url_for('authors.render_authors_list'))


@authors.route('/<int:author_id>/books', methods=['GET'])
def render_books_list_for_author(author_id: int):
    books = Book.query.all()
    author = Author.query.get(author_id)
    books_ids = [book.id for book in author.books]
    form = books_list_form_builder(books, books_ids)
    return render_template('author/attach_book_to_author.html', form=form, author_id=author_id)


@authors.route('/<int:author_id>/books', methods=['POST'])
def update_books_list_for_author(author_id: int):
    books = Book.query.all()
    form = books_list_form_builder(books, books_ids=[])

    if request.method == 'POST':
        if form.validate_on_submit():
            books_ids = select_values_by_key_prefix(
                key_prefix='book_',
                dictionary=request.form
            )
            author = Author.query.get(author_id)
            author.books = []
            for book_id in books_ids:
                book = Book.query.get(book_id)
                author.books.append(book)
            db.session.commit()

    return redirect(url_for('authors.render_author_details', author_id=author_id))


