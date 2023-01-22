# from wsgic.routing import Routes, Router
# from wsgic import WSGIApp

# index = lambda: "Hello World"

# router = Router(Routes().get("/", index))
# __app__ = WSGIApp(router)

# Or even simpler
from wsgic import WSGIApp
from wsgic.http import request, redirect
from wsgic.routing import Router, Routes

router = Router()
routes = router.get_routes()

routes.get("/redirect", lambda: redirect().next())
routes.get("/<name>", lambda name: "Hello %s" %name)
routes.get("/target", lambda: "Hello %s" %request.GET.name)

__app__ = app = WSGIApp(router)
