from wsgic.routing import Routes, Router
from .views import HomeView, BookView, source, target, Custom

router = Router()
routes = router.get_routes()
routes.set("<", ">", ":")

with routes.use(HomeView()):
	routes.get("/", callback="index", name="index")
	routes.get("new", callback="new")
	routes.get("test/<id:int>", callback="test")

routes.view("/books", BookView, name="books")
routes.view("/custom", Custom, name="custom")

routes.get("/source/<id:[a-z]:re>/", lambda id: "Hello", ignore="/")
routes.get("/target", target)
router.set_routes(routes)
