__author__ = 'hashbanger'

import uuid
import datetime
from database import Database


class Post(object):

    def __init__(self, blog_id, author, title, content, date = datetime.datetime.utcnow(), id = None):
        self.blog_id = blog_id
        self.author = author
        self.title = title
        self.content = content
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id 

    def save_to_mongo(self):
        Database.insert(collection = 'posts', data = self.json())

    @classmethod
    def get_from_mongo(cls, id):
        posts = Database.find_one(collection = 'posts', query = {'id': id})
        return cls(blog_id = post['blog_id'],
                    author = post['author'],
                    title = post['title'],
                    content = post['content'],
                    date = post['date'],
                    id = post['id'])

    def json(self):
        return {'blog_id' : self.blog_id,
                'author' : self.author,
                'title' : self.title,
                'content' : self.content,
                'date' : self.created_date,
                'id' : self.id
                }

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection = 'posts', query = {'blog_id': id})]