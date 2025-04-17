from src.schemas.user import UserCreate


class LoginRequest(UserCreate):
    pass


class RegisterRequest(UserCreate):
    pass
