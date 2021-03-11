from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Author
from app.forms import AddAuthor

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
