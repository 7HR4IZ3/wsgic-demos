from wsgic.database.columns import *
from wsgic.thirdparty.bottle import cached_property
from wsgic_auth.models import User

from .helpers import database as db, media

images = media["images"].create()

class Tag(db.Model):
    pass

class Rating(db.Model):
    item_id: int = ForeignKeyColumn(Tag, null=False)
    user: int = ForeignKeyColumn(User, null=False)
    value: int = IntegerColumn(max=5, min=1, null=False)

class Review(db.Model):
    title: str = Column(null=False)
    user: int = ForeignKeyColumn(User)
    game_id: int = IntegerColumn(null=False)
    rating: int = IntegerColumn(null=False)
    body: str = RichTextColumn(null=False)
    likes: int = IntegerColumn(min=0, default=0)
    dislikes: int = IntegerColumn(min=0, default=0)

class Game(db.Model):
    title: str = Column(null=False)
    images: str = ImageColumn(multiple=True, store=images, null=False)
    description: str = RichTextColumn(editor="bubble", null=False)
    date: datetime = DateTimeColumn()
    author: str = ForeignKeyColumn(User)
    active: int = BooleanColumn()
    tags: str
    ratings: str = OneToManyColumn(Rating)
    reviews: str = OneToManyColumn(Review)


    def __str__(self):
        return f"Game(id={self.id}, title={self.title}, author={self.author}, images={self.images}" + (" *)" if not self.active else ")")
    
    # @cached_property
    # def ratings(self):
    #     return Rating.objects.get(item_id=self.id)
    
    # @cached_property
    # def ratings_count(self):
    #     ret = {}
    #     for rating in self.ratings:
    #         if rating.value in ret:
    #             ret[rating.value] += 1
    #         else:
    #             ret[rating.value] = 1
    #     return ret
    
    # @cached_property
    # def ratings_avg(self):
    #     return sum([self.ratings_count[x] for x in self.ratings_count]) / len(self.ratings)
    
    @property
    def reviews(self):
        return Review.objects.get(game_id=self.id)
    
    @cached_property
    def excerpt(self):
        return " ".join(self.description.split(" ")[:48])
    
    @cached_property
    def date_formatted(self):
        return self.date.strftime("%d %B, %Y")

# db.backup(SqliteDatabase("./backup.db", check_same_thread=False))