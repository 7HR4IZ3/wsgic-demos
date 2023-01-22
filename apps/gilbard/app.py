from wsgic import WSGIApp
from wsgic.helpers import config

class GilbardApp(WSGIApp):
    def __init__(self):
        super().__init__("gilbard.urls:router", config)

__app__ = GilbardApp()
