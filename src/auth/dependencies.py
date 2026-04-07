from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, status
from .utils import decode_token


class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)

        token = creds.credentials
        token_data = decode_token(token)

        if not self.token_vaild(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please Provide an access token",
            )
        return token_data

    def token_vaild(self, token: str) -> bool:
        token = decode_token(token)
        return True if token is not None else False
