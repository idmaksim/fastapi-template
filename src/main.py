from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from src.routes import media_routes
from src.env import check_env
from src.routes import user_routes
from src.middlewares.logger import ProcessTimeMiddleware
from src.routes import auth_routes


# App initialization
async def lifespan(app: FastAPI):
    # Startupcsl
    check_env()
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    yield


app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(ProcessTimeMiddleware),
    ],
    lifespan=lifespan,
    swagger_ui_parameters={
        "tryItOutEnabled": True,
        "persistAuthorization": True,
    },
)


@app.get("/health")
async def health():
    return {"status": "ok"}


# Include routers
app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(media_routes.router)
