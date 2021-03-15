from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from app.models import Book, Reader


class AddReader(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    lastname = StringField("Nazwisko", validators=[DataRequired()])
    button = SubmitField("Dodaj")


class UpdateReader(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    lastname = StringField("Nazwisko", validators=[DataRequired()])
    button = SubmitField("Zaktualizuj")


class AddBook(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    genre = StringField("Gatunek", validators=[DataRequired()])
    button = SubmitField("Dodaj")


class UpdateBook(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    genre = StringField("Gatunek", validators=[DataRequired()])
    button = SubmitField("Zaktualizuj")


class AddAuthor(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    lastname = StringField("Nazwisko", validators=[DataRequired()])
    button = SubmitField("Dodaj")


def inventory_form_builder():
    class AddToInventory(FlaskForm):
        pass

    books = Book.query.all()
    select_list = [(book.id, book.title) for book in books]
    setattr(AddToInventory, 'book', SelectField('Książka', choices=select_list))
    setattr(AddToInventory, 'button', SubmitField('Dodaj'))

    return AddToInventory()


def assign_reader_form_builder():
    class AssignReaderForm(FlaskForm):
        pass
    readers = Reader.query.all()
    select_list = [(reader.id, f"{reader.name} {reader.lastname}") for reader in readers]
    setattr(AssignReaderForm, 'reader', SelectField('Czytelnik', choices=select_list))
    setattr(AssignReaderForm, 'button', SubmitField('Dodaj'))
    return AssignReaderForm()


def books_list_form_builder(books, books_ids):
    class BooksListForm(FlaskForm):
        pass

    for index, book in enumerate(books):
        if book.id in books_ids:
            setattr(BooksListForm, f"book_{index}", BooleanField(label=book.title, render_kw={
                'value': book.id,
                'checked': True
            }))
        else:
            setattr(BooksListForm, f"book_{index}", BooleanField(label=book.title, render_kw={'value': book.id}))
    setattr(BooksListForm, 'button', SubmitField('Przypisz'))
    return BooksListForm()


def authors_list_form_builder(authors, authors_ids):
    class AuthorsListForm(FlaskForm):
        pass

    for index, author in enumerate(authors):
        if author.id in authors_ids:
            setattr(AuthorsListForm, f"auth_{index}", BooleanField(label=str(author), render_kw={
                'value': author.id,
                'checked': True
            }))
        else:
            setattr(AuthorsListForm, f"auth_{index}", BooleanField(label=str(author), render_kw={'value': author.id}))
    setattr(AuthorsListForm, 'button', SubmitField('Przypisz'))
    return AuthorsListForm()


def select_values_by_key_prefix(key_prefix: str, dictionary) -> list:
    result_list = []
    for key, value in dictionary.items():
        if key[:len(key_prefix)] == key_prefix:
            result_list.append(value)
    return result_list
