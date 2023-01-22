from wsgic.base.models import Model, Field

class Blog(Model):
	def __init__(self):
		super().__init__()
		self.column.name = Field(type="text")
		self.column.title = Field(type="text", null=False)
		self.column.rating = Field(type="integer", default=1)
		self.create()
