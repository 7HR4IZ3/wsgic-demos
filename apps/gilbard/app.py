from wsgic import WSGIApp

class GilbardApp(WSGIApp):
    def __init__(self):
        super().__init__("gilbard.urls:router")

__app__ = GilbardApp()
