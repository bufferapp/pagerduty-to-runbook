from .sqlite import IncidentKeyLocatorSqlLite

INCIDENT_KEY_LOCATOR=None

def initializeDataStrategy(dataStrategy):
    global INCIDENT_KEY_LOCATOR
    if dataStrategy=="sqlite":
        INCIDENT_KEY_LOCATOR=IncidentKeyLocatorSqlLite

