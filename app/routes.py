from app import app, reader, book, author, inventory
from flask import render_template


@app.route('/')
def render_index_page():
    return render_template('index.html')


app.register_blueprint(reader.readers)
app.register_blueprint(book.books)
app.register_blueprint(author.authors)
app.register_blueprint(inventory.inventory)
