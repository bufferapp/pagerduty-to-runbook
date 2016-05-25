class User:
    def __init__(self, email, username, realName, profileStatus, password=""):
        self.email = email
        self.username = username
        self.realName = realName
        self.password = password
        self.profileStatus = profileStatus
