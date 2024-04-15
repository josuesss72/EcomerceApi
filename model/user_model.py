import re
from pydantic import BaseModel, root_validator


class User(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

    @root_validator()
    def root_validator(cls, values):
        confirm_password, password, email = (
            values.get("confirm_password"),
            values.get("password"),
            values.get("email"),
        )

        isEmail = lambda x: re.match(r"^[a-zA-Z0-9_.+-]+@(gmail\.com)$", x)

        if confirm_password != password:
            raise ValueError("Confirm password not is igual to password")
        if not isEmail(str(email)):
            raise ValueError("Email isnt correctly formatted jhon@gmail.com")
        return values


class UserUpdate(BaseModel):
    name: str
