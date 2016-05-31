from flask import session,url_for,request,redirect,render_template, send_file
from .. import application
from ..controllers import WebHookController

import configparser
import os
import logging
import requests

BASEPATH = '/api'
c = configparser.ConfigParser()
c.read('config.ini')
WEBHOOKPATH = c['ENDPOINT']['endPoint']
SLACKENDPOINT = c['ENDPOINT']['slack']

@application.route(BASEPATH+'/'+WEBHOOKPATH, methods=['GET', 'POST'])
def webhook():
    r = request.args
    logging.basicConfig(filename='/logs/loggers.log', level=logging.DEBUG)
    logging.debug(request.json)
    incident_runbook = WebHookController.getRunBookFromWebHookPing(request.json) 
    if incident_runbook["result"] == "success":
        requests.post(SLACKENDPOINT, json={"text":"Runbook document for above incident is: %s"%incident_runbook['value'].runbook_url})
        return "ok"
    else:
        requests.post(SLACKENDPOINT, json={"text":"Runbook document for above incident does not exist yet"})
        return "none"
