from ..users.User import User
from ..users import UserCRUD

def registerUser(email,username,realName, status, password, dataStrategy):
    return UserCRUD.saveUser(User(email,username,realName, status), password, dataStrategy)
