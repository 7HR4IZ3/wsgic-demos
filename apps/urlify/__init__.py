import secrets
from wsgic import WSGIApp
from wsgic.http import redirect, request
from wsgic.routing import Router, route
from wsgic.thirdparty.bottle import WebsocketPlugin
from wsgic.thirdparty.virtual_dom import VirtualDom, BaseContext, Reactive

from .models import Urls, datetime

router, routes = Router().get_routes()
routes.set("{", "}")
routes.install(WebsocketPlugin)

with open("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\wsgic\\thirdparty\\virtual_dom\\jyserver\\jyserver.js") as f:
    JYSERVER = f.read()

JYSERVER_AFTER = """
observer.observe(document.documentElement, {attributes: true, childList: true, characterData: true, subtree: true});
"""

def generate_short():
    return secrets.token_urlsafe(8)

class AppContext(BaseContext):
    count = Reactive()

    def __init__(self):
        super().__init__()
        self.count = 0

    def generate_url(self):
        url = self.browser.document.querySelector("input").value
        short = generate_short()
        
        Urls.objects.create(
            short=short, target=url, created=datetime.now()
        )

        gen = f"{str(request.url)[:-9]}/{short}"

        self.browser.document.querySelector("body").innerHTML = str(
            html.div(
                html.p(f"Recieved short link: "),
                html.a(gen, href=gen, target="_blank")
            )
        )

dom = VirtualDom(context=AppContext)
html = dom.HTML

r = routes.get("/websocket_server__", callback=dom.websocket)
print(r)

@routes.get("/")
def index():
    return f"Hello World from {request.path}"

@routes.add("/generate", methods=["GET", "POST"], name="generate")
def generate():
    if request.method == request.methods.GET:
        target = request.GET.get("target", "")
        return str(
            html.div(
                html.script(JYSERVER, type="text/javascript"),
                html.label(
                    "Target Url",
                    html.input(value=target, type="url", name="target"),
                ),
                html.button("Submit", onclick=dom.context.generate_url),
                html.script(JYSERVER_AFTER, type="text/javascript"),
                id="form"
            )
        )
    else:
        data = request.forms
        target = data.get("target", "").strip()
        short = generate_short()
        
        Urls.objects.create(
            short=short, target=target, created=datetime.now()
        )

        url = f"{str(request.url)[:-9]}/{short}"

        return html(
            html.body(
                html.div(
                    html.p(f"Recieved short link: "),
                    html.a(url, href=url, target="_blank")
                )
            )
        )

@routes.get("/{url}")
def goto(url):
    urlitem = Urls.objects.get(short=url)
    if urlitem:
        target = urlitem.target
        return redirect(target)
    else:
        return html.div(
            html.h1(f"Url for {url} not found..."),
            html.a("Create one now..", href=route("generate", query={"target": url}))
        )

__app__ = WSGIApp(router)
application = __app__.wrapped_app("wsgi")
