users = {}

def saveUser(user):
    users[user.username] = user
    return True

def getUser(username):
    return users.get(username)

def alterUser(user):
    users.update([username,user])
    return True

def getUserCount():
    return len(users.keys())

def deleteUser(user):
    users.pop("adnan")
    return True
