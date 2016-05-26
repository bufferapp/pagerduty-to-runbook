import json

class WebHookDataConverter():
    def __init__(self, data):
        self.data = json.loads(data)
        if self.isMessageATriggerType():
            for message in self.data['messages']:
                if message['type'] == "incident.trigger":
                    self.incident_key = message['data']['incident']['incident_key']
                    if self.incident_key == "null":
                        self.incident_key = None
        else:
            self.incident_key = None


    def isMessageATriggerType(self):
        if 'messages' in self.data:
            for message in self.data['messages']:
                if message['type'] == "incident.trigger":
                    return True
            return False
