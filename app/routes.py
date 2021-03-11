from app import app, reader
from flask import render_template


@app.route('/')
def render_index_page():
    return render_template('index.html')


app.register_blueprint(reader.readers)
