from wsgic.views import View
from wsgic.thirdparty import jinja2_template as render
from wsgic.server import request
import asyncio

#from auth.helpers import auth
from books.models import Book

def index():
	return Book.objects.all().json()

def new():
	name = request.GET.name
	title = request.GET.title

def test(id):
	#auth.login_required(fail_redirect=url("login"))
	return f"Getting Data on {id}"

def set(session, name):
    session['name'] = name
    return 'Set session name as %s'%name

def get(session, ):
    return 'Current session: name = "%s"'%session.get('name')

def test2(id):
	yield "Hello"
	yield " Tested"
	yield " %s"%str(id)
