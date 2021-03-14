from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


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
            setattr(BooksListForm, f"book_{index}", BooleanField(label=book.title, render_kw={'value': book.id,}))
    setattr(BooksListForm, 'button', SubmitField('Przypisz'))
    return BooksListForm()