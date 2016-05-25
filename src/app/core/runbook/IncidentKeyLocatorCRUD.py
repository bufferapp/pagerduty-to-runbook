def getIncidentKeyLocatorByIncidentKey(incident_key, incidentKeyLocatorDataStrategy):
    result = incidentKeyLocatorDataStrategy.getIncidentKeyLocatorByIncidentKey(incident_key)
    if result:
        return {"result": "success", "value": result}
    else:
        return {"result": "error"}
