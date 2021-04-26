import uuid

import datetime

from src.common.database import Database

from src.models.post import Post


class Blog(object):

    def __init__(self, author, title, description, author_id, created_date=datetime.datetime.utcnow(), _id=None):
        self.author = author

        self.author_id = author_id

        self.title = title

        self.description = description

        self.created_date = created_date

        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, created_date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,

                    title=title,

                    content=content,

                    author=author,

                    created_date=created_date)

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',

                        data=self.json())

    def json(self):
        return {

            'author': self.author,

            'author_id': self.author_id,

            'title': self.title,

            'description': self.description,

            'created_date': self.created_date

            '_id': self._id

        }

    @classmethod
    def from_mongo(cls, _id):
        blog_data = Database.find_one(collection='blogs', query={'_id': _id})

        return cls(author=blog_data['author'],

                   title=blog_data['title'],

                   description=blog_data['description'],

                   created_date=created_date['created_date']

        _id = blog_data['_id'])

        @classmethod
        def find_by_author_id(cls, author_id):
            blogs = Database.find(collection="blogs", query={'author_id': author_id})

            return [cls(**blog) for blog in blogs]