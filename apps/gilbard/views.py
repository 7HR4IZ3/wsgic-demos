from wsgic.views import render, FunctionView
from wsgic.http import request, redirect
from wsgic.services import service
from wsgic_auth.core.session import SessionAuth
from wsgic.routing.helpers import alias, named_route

from .models import Game
from .panels import *

authentication: SessionAuth = service("authentication")
validation = service("validation")

class HomeView(FunctionView):

    @named_route("homepage")
    def get_index(self):
        return render("index-2.html", { "games": Game.objects.all() })


class AuthView(FunctionView):

    @named_route("login")
    def get_login(self):
        if authentication.is_logged_in(): return redirect("/")
        return render("login.html")

    def post_login(self):
        if authentication.is_logged_in(): return redirect("/")

        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember_me", False) == "on"

        if validation.set_rules({
            "username": "required",
            "password": "required"
        }).validate(request.POST):
            authenticated = authentication.login(username, password, remember)
            if authenticated:
                return redirect().route("/").with_cookies()
            else:
                return redirect().back().error("Authentication failed.")
        else:
            error = validation.errors_list()
            return redirect().back().error(*error)

    def post_logout(self):
        if authentication.is_logged_in():
            authentication.logout()
        return redirect().to("/")