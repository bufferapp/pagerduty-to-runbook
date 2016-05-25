import unittest
from ..authentication import Register
from ..authentication import Login
from ..users.User import User
from . import InMemoryUserDataStrategy as dataStrategy

class TestAuthentication(unittest.TestCase):
    def tearDown(self):
        dataStrategy.users = {}
    def test_registerUser(self):
        self.assertEqual(True,Register.registerUser("test@example.com","test","Test Name", "admin", "pass1234", dataStrategy))
    def test_registerInvalidUser(self):
        self.assertIsNot(Register.registerUser("test@example.com","test","", "admin", "", dataStrategy), True)

    def test_loginUser(self):
        Register.registerUser("test@example.com","test","Test Name", "admin", "pass1234", dataStrategy)
        self.assertIsInstance(Login.loginUser("test","pass1234", dataStrategy)["success"], User)

    def test_loginUserWithInvalidCredentialsI(self):
        expectedErrorResult = {"error": "Invalid username or password"}
        Register.registerUser("test@example.com","test","Test Name", "admin", "pass1234", dataStrategy)
        self.assertEqual(expectedErrorResult,Login.loginUser("","pass1234", dataStrategy))
        self.assertEqual(expectedErrorResult,Login.loginUser("test","", dataStrategy))
        self.assertEqual(expectedErrorResult,Login.loginUser("","", dataStrategy))
        self.assertEqual(expectedErrorResult,Login.loginUser("testa","pass1234", dataStrategy))
        self.assertEqual(expectedErrorResult,Login.loginUser("test","pass123", dataStrategy))


if __name__ == "__main__":
    unittest.main()
