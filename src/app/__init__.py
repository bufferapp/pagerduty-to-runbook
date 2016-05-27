from flask import Flask, g
application=Flask(__name__,)
import configparser
from .routes import apiendpoints

c = configparser.ConfigParser()
c.read('config.ini')
application.secret_key=c['SECRETKEY']['secretKey']
