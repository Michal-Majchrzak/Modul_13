from app import db


book_details = db.Table('book_details',
                        db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                        db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
                        )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    lastname = db.Column(db.String(20), index=True)
    books = db.relationship('Book', secondary=book_details, lazy='subquery',
                            backref=db.backref('authors', lazy=True))

    def __str__(self):
        return f"<Author: {self.name} {self.lastname}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    genre = db.Column(db.String(20), index=True)

    def __str__(self):
        return f"<Book: {self.title[:50]} ..>"


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    lastname = db.Column(db.String(20), index=True)
    borrowed = db.relationship("InventoryUnit", backref="last_reader", lazy="dynamic")

    def __str__(self):
        return f"<Reader: {self.name} {self.lastname}>"


class InventoryUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    is_available = db.Column(db.Boolean)
    last_borrow_date = db.Column(db.DateTime, index=True)

    def __str__(self):
        return f"<InventoryUnit id[{self.id}] : Available: {self.is_available}>"
