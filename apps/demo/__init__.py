from wsgic import WSGIApp
from wsgic.routing.map import MapRouter

router = MapRouter()
routes = router.routes

@routes.get("/")
def index():
    return f"Hello World"

app = WSGIApp(router=router)
application = app.wrapped_app("wsgi")
