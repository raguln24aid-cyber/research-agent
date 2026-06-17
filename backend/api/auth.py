from fastapi import APIRouter, Depends

from api.deps import get_current_user
from schemas.auth import TokenResponse, UserLogin, UserResponse, UserSignup
from services.auth_service import AuthService
from utils.exceptions import AppException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=TokenResponse)
async def signup(data: UserSignup):
    try:
        return await AuthService().signup(data)
    except AppException as exc:
        raise _to_http(exc)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    try:
        return await AuthService().login(data)
    except AppException as exc:
        raise _to_http(exc)


@router.get("/me", response_model=UserResponse)
async def me(current_user: UserResponse = Depends(get_current_user)):
    return current_user


def _to_http(exc: AppException):
    from fastapi import HTTPException

    raise HTTPException(status_code=exc.status_code, detail=exc.message)
