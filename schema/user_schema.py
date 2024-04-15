from interfaces.user_interface import IUser


def user_Entity(item) -> IUser:
    return {
        "id": str(item.get("_id")),
        "name": item.get("name"),
        "email": item.get("email"),
        "password": item.get("password"),
        "created_at": item.get("created_at"),
        "update_at": item.get("update_at"),
    }


def users_Entities(entity):
    return [user_Entity(item) for item in entity]
