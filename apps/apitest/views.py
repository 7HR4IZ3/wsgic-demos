from wsgic_api.views import ApiView, SwaggerView
from wsgic_api.decorators.authentication import basicauth, tokenauth, sessionauth

from wsgic.http import request
from wsgic.routing import Routes
from wsgic.routing.helpers import limit, alias

from wsgic_auth.users import BaseUser
from wsgic_auth.core.token import TokenAuth

from .models import Product, Seller

routes = Routes()
token_auth = TokenAuth()

@routes.resource("/products")
class ProductsView(ApiView):
    model = Product
    response_type = "json"
    authenticators = [
        # tokenauth, basicauth, sessionauth
    ]

    def index(self):
        return []


@routes.resource("/sellers")
class SellersView(ApiView):
    model = Seller
    response_type = "json"
    authenticators = [
        # tokenauth, basicauth, sessionauth
    ]


@routes.expose
def generate():
    return token_auth.generate(BaseUser("admin"))


@routes.web_route("/calc")
def calc(send, get_browser):
    send("<p>1</p><button>add</button>")

    browser = get_browser()

    btn = browser.document.querySelector("button")
    p = browser.document.querySelector("p")

    def _(*a):
        p.innerText = str(int(p.innerText) + 1)

    btn.onclick = _
    browser.alert("Hello World")


@routes.websocket("/age")
def websocket(socket, close):
    socket.receive()

    socket.send("Name: ")
    name = socket.receive()
    print("Name:", name)
    socket.send(f"Hello {name}")

    close()
