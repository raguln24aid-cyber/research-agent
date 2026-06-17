from auth.jwt import create_access_token
from auth.password import hash_password, verify_password
from database.repositories.user_repository import UserRepository
from schemas.auth import TokenResponse, UserLogin, UserResponse, UserSignup
from utils.exceptions import ConflictError, UnauthorizedError


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    async def signup(self, data: UserSignup) -> TokenResponse:
        existing = await self.user_repo.find_by_email(data.email)
        if existing:
            raise ConflictError("Email already registered")

        hashed = hash_password(data.password)
        user = await self.user_repo.create(data.name, data.email, hashed)
        token = create_access_token(user["_id"], user["email"])
        return TokenResponse(
            access_token=token,
            user=UserResponse(
                id=user["_id"],
                name=user["name"],
                email=user["email"],
                created_at=user["created_at"],
            ),
        )

    async def login(self, data: UserLogin) -> TokenResponse:
        user = await self.user_repo.find_by_email(data.email)
        if not user or not verify_password(data.password, user["hashed_password"]):
            raise UnauthorizedError("Invalid email or password")

        token = create_access_token(user["_id"], user["email"])
        return TokenResponse(
            access_token=token,
            user=UserResponse(
                id=user["_id"],
                name=user["name"],
                email=user["email"],
                created_at=user["created_at"],
            ),
        )

    async def get_current_user(self, user_id: str) -> UserResponse:
        user = await self.user_repo.find_by_id(user_id)
        if not user:
            raise UnauthorizedError("User not found")
        return UserResponse(
            id=user["_id"],
            name=user["name"],
            email=user["email"],
            created_at=user["created_at"],
        )
