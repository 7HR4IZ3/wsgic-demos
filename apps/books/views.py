import json
from wsgic.http import request
from wsgic.thirdparty.bottle import redirect
from wsgic.views import FunctionView, View, BaseView

from .models import Book

class HomeView(BaseView):
	def index(self):
		return Book.json()

	def new(self):
		return "New Form"

	def test(self, id):
		return "Getting Data on %s" %id

class Custom(FunctionView):
	def get_():
		return "Homepage"
	
	def get_news(id):
		return

class BookView(View):
	def get(self):
		if request.get("id"):
			data = Book.id == int(self.request.id)
		else:
			data = Book.all()
		return json.dumps(data)
	
	def retrieve(self, id):
		pass
	
	def post(self):
		data = Book.new(title=self.request.title, rating=int(self.request.rating))
		return data.json()
	
	def put(self, id):
		data = Book.id == id

def source():
	return redirect("/target", source_url="/source")

def target():
	return "Redirected here from: %s"%request.session["source_url"]