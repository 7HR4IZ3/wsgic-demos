from wsgic.views import render
from wsgic.thirdparty.bottle import redirect as rdr
from wsgic.http import request, redirect, abort
from wsgic.session import sessions
from wsgic.services import service

from .models import Game
from .panels import *

authentication = service("authentication")
validation = service("validation")

lang = service("language")
lang.add_language("en", {
    "hello": "English Hello"
})
lang.add_language("de", {
    "hello": "Germany Hello"
})

def index(arg):
    # sessions.session["age"] = 5
    # sessions.save()
    try:
        if arg in ("", "/"):
            arg = "index-2.html"
        if arg == "favicon.ico":
            return abort(404)
        return render(arg)
    except Exception as e:
        raise e
        return abort(404)


def test1(name):
    sessions.session["name"] = name
    sessions.session.limit("name", 2)
    sessions.save()
    return "Set"

def test2():
    return str(sessions.session.get("name"))

def locale_test(name):
    return lang(name)

def login():
    # print(authentication.user())
    if request.user:
        return redirect("/")
    if request.method == request.methods.GET:
        return render("login.html")
    elif request.method in (request.methods.POST, request.methods.CLI):
        is_post = request.method == request.methods.POST
        data = request.POST if is_post else request.json
        
        username = data.get("username")
        password = data.get("password")
        remember = data.get("remember_me", False) == "on"

        if validation.set_rules({
            "username": "required",
            "password": "required"
        }).validate(data):
            authenticated = authentication.login(username, password, remember)
            if authenticated:
                return redirect().route("/").with_cookies()
            else:
                return redirect().back().error("Authentication failed.")
        else:
            error = request.validation.errors_list()
            if request.method == request.methods.CLI:
                return "\n".join(error)
            print(*error)
            return redirect().back().error(*error)

def logout():
    if authentication.is_logged_in():
        authentication.logout()
    return redirect().to("/")