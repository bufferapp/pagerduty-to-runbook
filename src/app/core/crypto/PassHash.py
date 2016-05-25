import bcrypt
SALT_LENGTH = 29
WORK_FACTOR = 7
def getHashedPassword(password):
    return bcrypt.hashpw(password, bcrypt.gensalt(WORK_FACTOR))
def getSaltedHashedPasword(password, salt):
    return bcrypt.hashpw(password, salt)
def matchPassWord(password, hashedPassword):
    return hashedPassword == getSaltedHashedPasword(password, hashedPassword[:SALT_LENGTH])
