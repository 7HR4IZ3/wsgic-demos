from wsgic_admin.panels import AdminPanel, register
from .models import *
from formify import HTML

html = HTML()

class GamePanel(AdminPanel):
    model = Game
    group = "Gilbard"

    columns = ["active", "author", "date", "excerpt", "images", "tags", "title"]

    def apply_data(self, column, instance):
        if column == "description":
            return instance.excerpt
        if column == "images":
            return ", ".join(html.a(x.filename, href=x.url) for x in instance.images)
        return instance[column]


class RatingPanel(AdminPanel):
    model = Rating
    group = "Gilbard"

class ReviewPanel(AdminPanel):
    model = Review
    group = "Gilbard"
    
class TagPanel(AdminPanel):
    model = Tag
    group = "Gilbard"

register(GamePanel, RatingPanel, ReviewPanel, TagPanel)
