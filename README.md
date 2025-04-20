# FastAPI Project Template 🚀

A modern, production-ready template for building scalable APIs with FastAPI.

## ✨ Features

- **FastAPI Framework** - High performance, easy to learn, fast to code, ready for production
- **SQLAlchemy Integration** - Powerful SQL toolkit and ORM
- **Alembic Migrations** - Database migrations made easy
- **Docker Support** - Containerization for consistent development and deployment
- **Environment Configuration** - Secure configuration management
- **JWT Authentication** - Secure authentication system
- **CORS Middleware** - Cross-Origin Resource Sharing support
- **API Documentation** - Automatic interactive API documentation
- **Logging** - Built-in logging configuration

## 🛠️ Prerequisites

- Python 3.10+
- uv (Python package manager)
- Docker (optional)

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/idmaksim/fastapi-template.git
cd fastapi-template
```

2. Sync dependencies:
```bash
uv sync
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

5. Run the application:
```bash
# Run the application in development mode
task dev

# Run the application in production mode
task prod
```

The API will be available at `http://localhost:8000`
API documentation will be at `http://localhost:8000/docs`

## 🐳 Docker Setup

1. Build the Docker image:
```bash
docker build -t fastapi-template .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 fastapi-template
```


## 🧪 Running Tests

```bash
pytest
```

## 📚 API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## ✨ Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
