__author__ = 'hashbanger'

from models.post import Post
from database import Database

Database.initialize()

post = Post(123, 'prashant', 'some title', 'some content')
post.save_to_mongo()
post.get_from_mongo()