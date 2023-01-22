from wsgic.base.views import View
from wsgic.server import render

class HomeView(View):
	def __init__(self):
		super().__init__(self)

	def index(self):
		return render("index.html")
