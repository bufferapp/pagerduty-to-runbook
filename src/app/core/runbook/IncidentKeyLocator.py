class IncidentKeyLocator():
    def __init__(self, incident_key, runbook_url):
        self.incident_key = incident_key
        self.runbook_url = runbook_url

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
