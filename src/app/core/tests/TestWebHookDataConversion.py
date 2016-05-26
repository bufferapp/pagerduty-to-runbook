import unittest
import json

from ..pagerduty.WebHookDataConverter import WebHookDataConverter

class TestWebHookDataConversion(unittest.TestCase):
    def setUp(self):
        self.testDataString = """
{
  "messages": [
    {
      "id": "bb8b8fe0-e8d5-11e2-9c1e-22000afd16cf",
      "created_on": "2013-07-09T20:25:44Z",
      "type": "incident.trigger",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "triggered",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "null",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:44Z",
          "last_status_change_by": "null"
        }
      }
    },
    {
      "id": "8a1d6420-e9c4-11e2-b33e-f23c91699516",
      "created_on": "2013-07-09T20:25:45Z",
      "type": "incident.resolve",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "resolved",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "null",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": "null",
          "resolved_by_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:45Z",
          "last_status_change_by": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          }
        }
      }
    }
  ]
}
"""
        self.testWebHookDataConverter = WebHookDataConverter(self.testDataString)

    def test_dataConverterObjectCreatesCorrectly(self):
        self.assertEqual(self.testWebHookDataConverter.data, json.loads(self.testDataString))
        self.assertIsNone(self.testWebHookDataConverter.incident_key)
        testConverterWithIncidentName = WebHookDataConverter("""
{
  "messages": [
    {
      "id": "bb8b8fe0-e8d5-11e2-9c1e-22000afd16cf",
      "created_on": "2013-07-09T20:25:44Z",
      "type": "incident.trigger",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "triggered",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "samplekey",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:44Z",
          "last_status_change_by": "null"
        }
      }
    },
    {
      "id": "8a1d6420-e9c4-11e2-b33e-f23c91699516",
      "created_on": "2013-07-09T20:25:45Z",
      "type": "incident.resolve",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "resolved",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "samplekey",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": "null",
          "resolved_by_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:45Z",
          "last_status_change_by": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          }
        }
      }
    }
  ]
}
""")
        self.assertEqual(testConverterWithIncidentName.incident_key, "samplekey")
    def test_dataConverterCanRecognizeObjectType(self):
        self.assertTrue(self.testWebHookDataConverter.isMessageATriggerType)
        self.testDataString = """
{
  "messages": [
    {
      "id": "bb8b8fe0-e8d5-11e2-9c1e-22000afd16cf",
      "created_on": "2013-07-09T20:25:44Z",
      "type": "incident.",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "triggered",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "null",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:44Z",
          "last_status_change_by": "null"
        }
      }
    },
    {
      "id": "8a1d6420-e9c4-11e2-b33e-f23c91699516",
      "created_on": "2013-07-09T20:25:45Z",
      "type": "incident.resolve",
      "data": {
        "incident": {
          "id": "PIJ90N7",
          "incident_number": 1,
          "created_on": "2013-07-09T20:25:44Z",
          "status": "resolved",
          "html_url": "https://acme.pagerduty.com/incidents/PIJ90N7",
          "incident_key": "null",
          "service": {
            "id": "PBAZLIU",
            "name": "service",
            "html_url": "https://acme.pagerduty.com/services/PBAZLIU"
          },
          "assigned_to_user": "null",
          "resolved_by_user": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          },
          "trigger_summary_data": {
            "subject": "45645"
          },
          "trigger_details_html_url": "https://acme.pagerduty.com/incidents/PIJ90N7/log_entries/PIJ90N7",
          "last_status_change_on": "2013-07-09T20:25:45Z",
          "last_status_change_by": {
            "id": "PPI9KUT",
            "name": "Alan Kay",
            "email": "alan@pagerduty.com",
            "html_url": "https://acme.pagerduty.com/users/PPI9KUT"
          }
        }
      }
    }
  ]
}
"""
        self.testWebHookDataConverter = WebHookDataConverter(self.testDataString)
        self.assertTrue(self.testWebHookDataConverter.isMessageATriggerType)

if __name__ == "__main__":
    unittest.main()
