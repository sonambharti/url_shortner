# app/core/exception_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from jwt import ExpiredSignatureError, InvalidTokenError
from starlette.middleware.base import BaseHTTPMiddleware
import traceback

class JWTExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ExpiredSignatureError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Access token has expired. Please log in again."},
            )
        except InvalidTokenError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token. Please log in again."},
            )
        except Exception as e:
            traceback.print_exc()
            return JSONResponse(
                status_code=500,
                content={"detail": f"Internal Server Error: {str(e)}"},
            )
