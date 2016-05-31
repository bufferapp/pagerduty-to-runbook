from ..core.pagerduty.WebHookDataConverter import WebHookDataConverter
from ..core.runbook import IncidentKeyLocatorCRUD
from ..data import DataStrategy
import json

def getRunBookFromWebHookPing(pagerdutyMessage):
    data_converter = WebHookDataConverter(json.dumps(pagerdutyMessage))
    if data_converter.isMessageATriggerType():
        incident = IncidentKeyLocatorCRUD.getIncidentKeyLocatorByIncidentKey(data_converter.incident_key, DataStrategy.INCIDENT_KEY_LOCATOR)
        return incident
    
