from .views import HomeView
hv = HomeView()

mount = "/"

routes = {}
routes['/'] = (hv.index, ["GET", "POST"], "homepage")
