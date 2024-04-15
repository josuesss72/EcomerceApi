from datetime import timedelta
from model.auth_model import auth


def login(formData):
    user = auth.authentication(formData.username, formData.password) 
    accessTokenExpires = timedelta(minutes=30)
    accessTokenJWT = auth.createToken({"sub": user.get("email")}, accessTokenExpires)
    return {
        "access_token": accessTokenJWT,
        "token_type": "bearer",
    }
