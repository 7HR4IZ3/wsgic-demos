from wsgic_auth.scripts import setup_demo, script

from .models import Product
from datetime import date
import json

demo_data = [
	{
		"name": "Apple",
		"price": 15,
		"date": date.today()
	}, {
		"name": "Banana",
		"price": 19,
		"date": date.today()
	}, {
		"name": "Pawpaw",
		"price": 10,
		"date": date.today()
	}, {
		"name": "Watermelon",
		"price": 30,
		"date": date.today()
	}, {
		"name": "Pineapple",
		"price": 20,
		"date": date.today()
	}, {
		"name": "Grape",
		"price": 18,
		"date": date.today()
	}, {
		"name": "Berries",
		"price": 80,
		"date": date.today()
	}
]

@script("setup-demo")
def setup_demo(data=None):
	if data:
		data = json.loads(data)
	else:
		data = demo_data
	for item in data:
		Product.objects.create(**item)
