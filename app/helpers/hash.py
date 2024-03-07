from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def hash_password(password: str):
        # Hash a password with a randomly-generated salt
       return pwd_context.hash(password)

    def verify_password(input_password: str, hashed_password: str):
        # Check if the input password matches the hashed password
         return pwd_context.verify(input_password, hashed_password)