from dotenv import dotenv_values

import os


class Config:
    SECRET_KEY = os.urandom(16).hex()
    SQLALCHEMY_DATABASE_URI = dotenv_values('.env')['DATABASE_URI']