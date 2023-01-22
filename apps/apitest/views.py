from wsgic_api.views import ApiView
from wsgic_api.decorators.authentication import basicauth, tokenauth, sessionauth

from wsgic.http import request
from wsgic.routing import Routes
from wsgic.routing.helpers import limit, alias

from wsgic_auth.users import BaseUser
from wsgic_auth.core.token import TokenAuth

from .models import Product, Seller

routes = Routes()
tokenauthentication= TokenAuth()

@routes.resource("/")
class ProductsView(ApiView):
    model = Product
    response_type = "json"
    authenticators = [
        tokenauth, basicauth, sessionauth
    ]

@routes.resource("/sellers")
class SellersView(ApiView):
    model = Seller
    response_type = "json"
    authenticators = [
        tokenauth, basicauth, sessionauth
    ]

@routes.expose
def generate():
    return tokenauthentication.generate(BaseUser("admin"))
