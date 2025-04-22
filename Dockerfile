FROM python:3.11-slim


COPY . /app

WORKDIR  /app

RUN pip install uv

RUN python -m venv .venv
RUN . .venv/bin/activate && uv sync --no-dev


CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]