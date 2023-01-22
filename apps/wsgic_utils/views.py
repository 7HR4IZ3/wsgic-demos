from wsgic.http import request

def index():
    return "Hello World from {request.path}"
