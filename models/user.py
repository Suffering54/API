import uuid

import datetime

from common.database import Database

from flask import session


class User(object):

    def __init__(self, email, password, _id=None):

        self.email = email

        self.password = password

        self._id = uuid.uuid4().hex if _id is None else _id

    def get_by_email(self):

        data = Database.find_one("users", {"email": self.email})

        if data is not None:
            return cls(**data)

    def get_by_id(self):

        data = Database.find_one("users", {"_id": self._id})

        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):

        user = User.get_by_email(email)

        if user is not None:
            return user.password == password

        return false

    @classmethod
    def register(cls, email, password):

        user = cls.get_by_email(email)

        if user is None:

            new_user = cls(email, password)

            new_user.save_to_mongo()

            session['email'] = email

            return True

        else:

            return False

    def save_to_mongo(self):

        Database.insert("users", self.json())

    @staticmethod
    def login(user_email):

        # method login_valid already been called so we stock in session

        session['email'] = user_email

    @staticmethod
    def logout():

        session['email'] = None

    def json(self):

        return {

            "email": self.email,

            "_id": self._id,

            "password": self.password

        }

    def get_blogs(self):

        return Blog.find_by_author_id(self.id)

    def new_blog(self, title, description, created_date=datetime.datetime.utcnow()):

        blog = Blog(author=self.email, title=title, description=description, author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):

        blog = Blog.from_mongo(blog_id)

        blog.new_post(title=title, content=content, date_created=date)