from wsgic.database.columns import *
from .helpers import database as db

# SqlalchemyDatabase
# class Books(db.Model):
# 	__tablename__ = "books"
# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(128))
#	rating = Column(Integer, default=1)

# JsonDatabase
# Books = db.table("Books", {
# 	"title": db.column("text", max_length=50),
# 	"rating": db.column("integer", default=1)
# })
# db.commit()

# SqlteDatabase
# class Books(db.Model):
# 	def __init__(self):
# 		super().__init__()
# 		self.column('name', type="text")
# 		self.column('title', type="text", null=False)
# 		self.column('rating', type="integer", default=1)
# db.create(Books)

class Book(db.Model):
	name: str
	title: str = Column(null=False)
	rating: int = 1

class Author(db.Model):
	name: str
	books: str = OneToManyColumn(Book, backref="author")
