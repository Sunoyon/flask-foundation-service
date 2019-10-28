from app.entities.author import Author
from app.entities.db import db


def save(author):
    db.session.add(author)
    db.session.commit()
    return author


def get_by_id(author_id):
    return Author.query.get(author_id)
