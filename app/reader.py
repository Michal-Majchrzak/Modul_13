from flask import render_template, Blueprint, request, redirect, url_for
from app import db
from app.models import Reader
from app.forms import AddReader, UpdateReader

readers = Blueprint('readers', __name__, url_prefix='/readers')


@readers.route('/list', methods=['GET'])
def render_readers_list():
    readers_list = Reader.query.all()
    return render_template('/reader/readers_list.html', readers_list=readers_list)


@readers.route('/add', methods=['GET'])
def render_add_reader():
    form = AddReader()
    return render_template('/reader/readers_list.html', form=form)


@readers.route('/add', methods=['POST'])
def add_reader_to_db():
    form = AddReader()
    if request.method == 'POST':
        if form.validate_on_submit():
            reader = Reader(
                name=request.form.get('name'),
                lastname=request.form.get('lastname')
            )
            db.session.add(reader)
            db.session.commit()
            return redirect(url_for('readers.render_readers_list'))


@readers.route('/update/<int:reader_id>', methods=['GET'])
def render_update_reader(reader_id: int):
    reader = Reader.query.get(reader_id)
    form = UpdateReader(data={
        'name': reader.name,
        'lastname': reader.lastname
    })
    return render_template('/reader/update_reader.html', form=form, reader_id=reader_id)


@readers.route('/update/<int:reader_id>', methods=['POST'])
def update_reader_to_db(reader_id: int):
    form = UpdateReader()
    if request.method == 'POST':
        if form.validate_on_submit():
            reader = Reader.query.get(reader_id)
            reader.name = request.form.get('name')
            reader.lastname = request.form.get('lastname')
            db.session.add(reader)
            db.session.commit()
            return redirect(url_for('readers.render_readers_list'))


@readers.route('/<int:reader_id>/delete', methods=['GET'])
def delete_reader_by_id(reader_id: int):
    reader = Reader.query.get_or_404(reader_id)
    db.session.delete(reader)
    db.session.commit()
    return redirect(url_for('readers.render_readers_list'))