from ...core.runbook.IncidentKeyLocator import IncidentKeyLocator
import sqlite3
import logging

def getIncidentKeyLocatorByIncidentKey(incident_key):
    logging.basicConfig(filename='/logs/loggers.log', level=logging.DEBUG)
    logging.debug(incident_key)
    conn = sqlite3.connect('/data/data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT incident_key, runbook_url FROM runbooks WHERE incident_key=:incident_key",{"incident_key": incident_key})
    res = cur.fetchone()
    if res:
        logging.debug(res.keys())
        incident = IncidentKeyLocator(res['incident_key'], res['runbook_url'])
        return incident

