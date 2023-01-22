import requests
from jwt import PyJWT
from requests.auth import HTTPBasicAuth, HTTPDigestAuth, HTTPProxyAuth, AuthBase

class JWTAuth(AuthBase):
    def __init__(self, token):
        self.token = token
        self.key = "my-secret-key"
        #self.token = PyJWT().encode(self.token, self.key)

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer " + self.token
        return r

url = "http://localhost:8100/details"

def generate(username, password):
    a = requests.get(url+"bauth", auth=HTTPBasicAuth(username, password))
    print(a.text)
    b = requests.get(url+"generate", cookies=a.cookies)
    print(b.text)

def retrieve(text):
    c = requests.get(url, auth=JWTAuth(text))
    print(c.text)

# import sys
# args = sys.argv[1:]

# if args[0] == "gen":
#     generate(args[1], args[2])
# elif args[0] == "ret":
#     retrieve(args[1])

retrieve("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJwZXJtaXNzaW9ucyI6W1tdLFtdXX0.hLJIqSeiWDSnBVuYcDFLA6MAG119T_-o7Lrj0y_-CtQ")
