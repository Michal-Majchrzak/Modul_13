from app import db


book_author = db.Table('book_author',
                        db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                        db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
                        )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    lastname = db.Column(db.String(20), index=True)
    books = db.relationship('Book',
                            secondary=book_author,
                            back_populates="authors")

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    genre = db.Column(db.String(20), index=True)
    authors = db.relationship('Author',
                              secondary=book_author,
                              back_populates='books')
    inventory_items = db.relationship('InventoryItem', backref='book', lazy=True)

    def __str__(self):
        return f"<Book: {self.title[:50]} ..>"


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    lastname = db.Column(db.String(20), index=True)
    borrowed_books = db.relationship('InventoryItem', backref='reader', lazy=True)

    def __str__(self):
        return f"<Reader: {self.name} {self.lastname}>"


class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))

    def __str__(self):
        return f"<Item: {self.id} {self.book_id} {self.reader_id}>"
