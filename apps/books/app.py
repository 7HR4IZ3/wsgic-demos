from wsgic.apps import WSGIApp

class BooksApp(WSGIApp):
	pass

__app__ = BooksApp("books.urls:router")
