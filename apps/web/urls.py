from wsgic.routing import Router
from wsgic.apps import DjangoApp, FlaskApp, WsgicApp
from wsgic_admin import AdminApp
# from wsgic.session.plugins import SessionPlugin
from books.urls import routes as BookRoutes

from .views import index, test, new, get, set, test2
import uuid

router = Router()
routes = router.routes

routes.set("{", "}")
# routes.install(SessionPlugin())

routes.placeholder("uuid", r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", uuid.UUID, lambda x: str(x))

routes.add("/", index, method=["GET", "POST"], name="homepage")
routes.get("/test/{id :int}", test2, name="async")
routes.post("/new", new, name="new")
routes.get("/get", get)
routes.get("/set/{name}", set)

with routes.group("api"):
	routes.include(BookRoutes)

# routes.mount("static", DjangoApp(module="django.contrib.staticfiles"))
routes.mount("admin", AdminApp)
# routes.mount("django", DjangoApp(module="djng"))
# routes.mount("flask", "flas:app::flask")
# routes.mount("pyramid", "pyr.app::pyramid")


# routes.mount("auth", WsgicApp("auth"), name="wsgic")
