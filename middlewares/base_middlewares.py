from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response


class BaseMiddlewares(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        if request.url.path == "/api/user/{id}":
            response = await call_next(request)
        else:
            response = await call_next(request)
        return response
