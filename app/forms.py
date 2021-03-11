from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
