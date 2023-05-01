
from passlib.context import CryptContext

pw_cxt=CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return pw_cxt.hash(password)