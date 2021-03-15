from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import InventoryItem, Book, Reader
from app.forms import inventory_form_builder, assign_reader_form_builder

inventory = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory.route('/list', methods=['GET'])
def render_inventory_list():
    inv_items = InventoryItem.query.all()
    return render_template('inventory/inventory_list.html', inventory_items=inv_items)


@inventory.route('/add', methods=['GET'])
def render_add_inventory_form():
    form = inventory_form_builder()
    return render_template('inventory/add_inventory_item.html', form=form)


@inventory.route('/add', methods=['POST'])
def add_selected_book_to_inventory():
    form = inventory_form_builder()
    if request.method == 'POST':
        if form.validate_on_submit():
            book = Book.query.get(request.form.get('book'))
            inv_item = InventoryItem(book=book)
            db.session.add(inv_item)
            db.session.commit()
    return redirect(url_for('inventory.render_inventory_list'))


@inventory.route('/<int:item_id>/assign', methods=['GET'])
def render_assign_reader(item_id: int):
    item = InventoryItem.query.get(item_id)
    form = assign_reader_form_builder()
    return render_template('inventory/assign_reader.html', form=form, item=item)


@inventory.route('/<int:item_id>/assign', methods=['POST'])
def assign_reader_to_item(item_id: int):
    form = assign_reader_form_builder()
    if request.method == 'POST':
        if form.validate_on_submit():
            item = InventoryItem.query.get(item_id)
            reader = Reader.query.get(request.form.get('reader'))
            item.reader = reader
            db.session.add(item)
            db.session.commit()
    return redirect(url_for('inventory.render_inventory_list'))


@inventory.route('/<int:item_id>/delete', methods=['GET'])
def delete_item_by_id(item_id: int):
    item = InventoryItem.query.get(item_id)
    if not item:
        print(f"Inventory Item o numerze id : [{item.id}] nie istnieje.")
        return redirect(url_for('inventory.render_inventory_list'))
    else:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('inventory.render_inventory_list'))
