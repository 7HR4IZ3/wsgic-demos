# from bottle import Bottle, request
# from formify import HTML

# app = Bottle()
# html = HTML()

# @app.route("/", method=["GET", "POST"])
# def index():
#     if request.method == "GET":
#         return html.form(
#             html.input(type="text", placeholder="Enter Name", name="name"),
#             html.input(type="file", placeholder="Select file", name="file"),
#             html.input(type="submit"),
#             action="/", method="post", enctype="multipart/form-data"
#         )
#     elif request.method == "POST":
#         print({x: request.POST[x] for x in request.POST})
#         print({x: request.files[x] for x in request.files})

# app.run()
from lxml.html import diff
from bs4 import BeautifulSoup

with open("C:\\Users\\user.user-PC\\Downloads\\(5) 𝙈𝙤𝙤𝙙気分 _ Facebook_files\\Market Data - BBC News2.html", "r") as f:
    old = BeautifulSoup(f.read())
    old_body = old.find("body")

with open("C:\\Users\\user.user-PC\\Downloads\\(5) 𝙈𝙤𝙤𝙙気分 _ Facebook_files\\Market Data - BBC News.html", "r") as f:
    new = BeautifulSoup(f.read())
    new_body = new.find("body")

d = diff.htmldiff(
    str(old_body), str(new_body)
)

with open("C:\\Users\\user.user-PC\\Downloads\\(5) 𝙈𝙤𝙤𝙙気分 _ Facebook_files\\Market Data - BBC News diff.html", "w") as f:
    di = old.append(
        BeautifulSoup(d)
    )
    f.write(di.pr)
