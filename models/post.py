__author__ = 'hashbanger'

import uuid
from database import Database
import datetime

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

    def get_from_mongo(self):
        posts = Database.find(collection = 'posts', query = {})
        for post in posts:
            print('Blog_id: {}\nAuthor: {}\nTitle: {}\nContent: {}\nDate: {}\nID: {}'.format(post['blog_id'],
                                                                                            post['author'],
                                                                                            post['title'],
                                                                                            post['content'],
                                                                                            post['date'],
                                                                                            post['id']))
    
    def json(self):
        return {'blog_id' : self.blog_id,
                'author' : self.author,
                'title' : self.title,
                'content' : self.content,
                'date' : self.created_date,
                'id' : self.id
                }