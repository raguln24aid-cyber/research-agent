from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from auth.jwt import decode_access_token
from schemas.auth import UserResponse
from services.auth_service import AuthService
from utils.exceptions import UnauthorizedError

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserResponse:
    payload = decode_access_token(credentials.credentials)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    auth_service = AuthService()
    try:
        return await auth_service.get_current_user(payload["sub"])
    except UnauthorizedError as exc:
        raise HTTPException(status_code=401, detail=exc.message) from exc
