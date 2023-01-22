from wsgic import WSGIApp

class PortfolioApp(WSGIApp):
	def __init__(self):
		super().__init__(__package__)

def get_app():
	app = PortfolioApp()
	return app
