from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def getPasswordHash(password:str):
    return pwd_context.hash(password)

def verifyPassword(password:str, hashPassword):
    return pwd_context.verify(password, hashPassword)
