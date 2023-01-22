#from sqlalchemy import Column, ForeignKey, Integer, String
from wsgic.database.columns import *
from .helpers import database as db

class Book(db.Model):
	name: str
	title: str = Column(null=False)
	rating: int = 1

class Author(db.Model):
	name: str
	books: str = OneToManyColumn(Book, backref="author")
