from django.urls import path, include
from .views import *

urlpatterns = [
	path("", index),
	path("2", index2, name="index2"),
	path("3", index3, name="index3")
]
