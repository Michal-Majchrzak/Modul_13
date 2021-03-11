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
