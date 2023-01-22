from wsgic_auth.models import User
from .helpers import database, columns

class Product(database.Model):
	name: str = columns.Column(null=False)
	price: int = columns.IntegerColumn(min=0, null=False)
	date = columns.DateColumn(serialize=lambda date: date.isoformat())
	# seller = columns.BackRef("Seller")

# class DemoProduct(Product):
# 	class Meta:
# 		extends = [Product, User]
# 		db = database

class Seller(database.Model):
	user = columns.ForeignKeyColumn(User)
	products = columns.OneToManyColumn(Product)
