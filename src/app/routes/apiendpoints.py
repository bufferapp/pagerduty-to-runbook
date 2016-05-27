from flask import session,url_for,request,redirect,render_template, send_file
from .. import application
from ..controllers import WebHookController

import configparser
import os

BASEPATH = '/api'
c = configparser.ConfigParser()
c.read('config.ini')
WEBHOOKPATH = c['ENDPOINT']['endPoint']

@application.route(BASEPATH+'/'+WEBHOOKPATH, methods=['GET'])
def webhook():
    r = request.args
    print(request.args)
    return "api"
