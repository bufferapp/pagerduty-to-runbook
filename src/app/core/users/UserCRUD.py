from ..crypto import PassHash

def saveUser(userToSave, password, dataStrategy):
    validationResults = validateUser(userToSave, password)
    if(validationResults == True):
        userToSave.password = PassHash.getHashedPassword(bytes(password, "utf-8"))
        return dataStrategy.saveUser(userToSave)
    else:
        return validationResults

def getUser(username, dataStrategy):
    if(username == "" or not username):
        return None
    else:
        return dataStrategy.getUser(username)

def getNumberOfUsers(dataStrategy):
    return dataStrategy.getUserCount()

def validateUser(userToValidate, password):
    validationDict = {}
    if (not userToValidate.email or userToValidate.email == ""):
        validationDict["email"] = "Email cannot be empty"
    if (not userToValidate.username or userToValidate.username == ""):
        validationDict["username"] = "Username cannot be empty"
    if (not userToValidate.realName or userToValidate.realName == ""):
        validationDict["realName"] = "Name cannot be empty"
    if (not password or password == ""):
        validationDict["password"] = "Password cannot be empty"
    #TODO Add email validation logic
    #TODO Add alpha numeric logic 
    #TODO Validate password length
    if len(validationDict) ==0:
        return True
    else:
        return validationDict
