import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from src.logger import logger


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log request details
        logger.info(
            f"Request started: {request.method} {request.url.path} "
            f"Client: {request.client.host if request.client else 'Unknown'}"
        )

        try:
            response = await call_next(request)

            # Calculate process time
            process_time = time.time() - start_time

            # Log response details
            logger.info(
                f"Request completed: {request.method} {request.url.path} "
                f"Status: {response.status_code} "
                f"Process time: {process_time:.3f}s"
            )

            response.headers["X-Process-Time"] = str(process_time)
            return response

        except Exception as e:
            # Log error details
            logger.error(
                f"Request failed: {request.method} {request.url.path} Error: {str(e)}"
            )
            raise
