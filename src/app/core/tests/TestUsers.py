from ..users.User import User
from ..users import UserCRUD
import unittest
from . import InMemoryUserDataStrategy

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.testUser = User("test@example.com","testuser", "Test Name", "admin")
        self.testUserpass = "pass1234"
        self.dataStrategy = InMemoryUserDataStrategy

    def tearDown(self):
        InMemoryUserDataStrategy.users = {}

    def test_objectCreatedCorrectly(self):
        self.assertEqual(self.testUser.email,"test@example.com")
        self.assertEqual(self.testUser.username, "testuser")
        self.assertEqual(self.testUser.realName, "Test Name")
        self.assertEqual(self.testUser.profileStatus, "admin")

    def test_saveUser(self):
        self.assertTrue(UserCRUD.saveUser(self.testUser, "pass123", self.dataStrategy))

    def test_numberOfUsers(self):
        UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)
        UserCRUD.saveUser(User("test2@example.com", "test2user", "Test 2 Name", "customerservice"), "pass3456", self.dataStrategy)
        self.assertEqual(UserCRUD.getNumberOfUsers(self.dataStrategy), 2)

    def test_saveInvalidUser(self):
        self.testUser.email = ""
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["email"], "Email cannot be empty")
        self.testUser.email = None
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["email"], "Email cannot be empty")
        self.testUser.email = "test@example.com"
        self.testUser.username = ""
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["username"], "Username cannot be empty")
        self.testUser.username = None
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["username"], "Username cannot be empty")
        self.testUser.realName = ""
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["realName"], "Name cannot be empty")
        self.testUser.realName = None
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["realName"], "Name cannot be empty")
        self.testUserpass = ""
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["password"], "Password cannot be empty")
        self.testUser.password = None
        self.assertEqual(UserCRUD.saveUser(self.testUser, self.testUserpass, self.dataStrategy)["password"], "Password cannot be empty")

if __name__ == "__main__":
    unittest.main()        
