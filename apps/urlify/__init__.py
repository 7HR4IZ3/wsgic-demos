from wsgic import WSGIApp
from wsgic.http import redirect, request
from wsgic.routing import Router, route

import formify
import secrets

router, routes = Router().get_routes()
routes.set("{", "}")

urls = {}

html = formify.HTML()

def generate_short():
    return secrets.token_urlsafe(8)

@routes.get("/")
def index():
    return f"Hello World from {request.path}"

@routes.add("/generate", methods=["GET", "POST"], name="generate")
def generate():
    if request.method == request.methods.GET:
        target = request.GET.get("target", "")
        return html.center(
            html.form(
                html.label(
                    "Target Url",
                    html.input(value=target, type="url", name="target"),
                ),
                html.button("Submit", type="submit"),
                method="post"
            )
        )
    else:
        data = request.forms
        target = data.get("target", "").strip()
        short = generate_short()
        urls[short] = target

        url = f"{str(request.url)[:-9]}/{short}"

        return html.div(
            html.p(f"Recieved short link: "),
            html.a(url, href=url, target="_parent")
        )

@routes.get("/{url}")
def goto(url):
    if url in urls:
        target = urls[url]
        return redirect(target)
    else:
        return html.div(
            html.h1(f"Url for {url} not found..."),
            html.a("Create one now..", href=route("generate", query={"target": url}))
        )

__app__ = WSGIApp(router)
application = __app__.wrapped_app("wsgi")
