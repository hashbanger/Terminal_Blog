__author__ = 'hashbanger'

from database import Database 
from models.blog import Blog 

class Menu(object):
    def __init__(self):
        self.user = input('Enter author name : ')
        self.user_blog = None 
        if self._user_has_account():
            print('Welcome Back! {}'.format(self.user))
        else:
            self._prompt_user_for_account()
    
    def _user_has_account(self):
        blog = Database.find_one(collection = 'blogs', query = {'author' : self.user})
        if blog is not None:
            return True 
        else:
            return False 

    def _prompt_user_for_account(self):
        title = input('Enter blog title : ')
        description = input('Enter blog description : ')
        blog = Blog(author = self.user,
                    title = title,
                    description = description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input('Do you want to read (R) or write (W) blogs? : ')
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
            pass
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print('Thank You for being on Terminal Blog!')
        
    def _list_blogs(self):
        blogs = Database.find(collection = 'blogs',
                                query ={})
        for blog in blogs:
            print('\n\nID: {}\nTitle: {}\nAuthor: {}'.format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input('Enter the id of the blog you want to read : ')
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print('\n\nDate: {}\nTitle: {}\n\n{}'.format(post['date'], post['title'], post['content']))
