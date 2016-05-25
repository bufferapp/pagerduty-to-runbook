from ..crypto import PassHash
from ..users import UserCRUD

def loginUser(username,password, dataStrategy):
    user = UserCRUD.getUser(username, dataStrategy)
    if(user):
        if(PassHash.matchPassWord(bytes(password,"utf-8"), user.password)):
            return {"success": user}
    return {"error": "Invalid username or password"}
