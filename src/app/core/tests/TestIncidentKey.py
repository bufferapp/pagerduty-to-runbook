import unittest
from unittest.mock import Mock

from ..runbook.IncidentKeyLocator import IncidentKeyLocator
from ..runbook import IncidentKeyLocatorCRUD

class TestIncidentKeyLocator(unittest.TestCase):
    def setUp(self):
        self.testIncidentKeyLocatorObject = IncidentKeyLocator("pd_key", "http://examplerunbookurl.com")

    def test_incidentKeyLocatorObjectCreatesCorrectly(self):
        self.assertEqual(self.testIncidentKeyLocatorObject.incident_key, "pd_key")
        self.assertEqual(self.testIncidentKeyLocatorObject.runbook_url, "http://examplerunbookurl.com")

class TestIncidentKeyCRUD(unittest.TestCase):
    def setUp(self):
        self.testIncidentKeyLocatorObject = IncidentKeyLocator("pd_key", "http://examplerunbookurl.com")
        self.mockIncidentKeyLocatorDataStrategy = Mock()
        self.mockIncidentKeyLocatorDataStrategyAttrs = {"getIncidentKeyLocatorByIncidentKey.side_effect": [IncidentKeyLocator("pd_key", "http://examplerunbookurl.com"), None]}
        self.mockIncidentKeyLocatorDataStrategy.configure_mock(**self.mockIncidentKeyLocatorDataStrategyAttrs)

    def test_incidentKeyLocatedCanBeRetrievedByIncidentKey(self):
        result = IncidentKeyLocatorCRUD.getIncidentKeyLocatorByIncidentKey("pd_key", self.mockIncidentKeyLocatorDataStrategy)
        self.assertEqual(result["result"], "success")
        self.assertEqual(result["value"], self.testIncidentKeyLocatorObject)

    def test_incidentKeyNotLocatedReturnsCorrectResult(self):
        IncidentKeyLocatorCRUD.getIncidentKeyLocatorByIncidentKey("pd_key", self.mockIncidentKeyLocatorDataStrategy)
        result = IncidentKeyLocatorCRUD.getIncidentKeyLocatorByIncidentKey("pd_key", self.mockIncidentKeyLocatorDataStrategy)
        self.assertEqual(result["result"], "error")

if __name__ == "__main__":
    unittest.main()
