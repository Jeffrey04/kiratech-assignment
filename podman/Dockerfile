FROM python:3.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

RUN uv sync --frozen --no-editable --no-dev --compile-bytecode && \
    uv pip install -e .

# FIXME find out how to properly add libraries without requiring pyproject
#FROM gcr.io/distroless/python3-debian12:debug
#
#EXPOSE 8081/tcp
#
#COPY --from=builder /app/.venv /app/.venv

ENTRYPOINT ["/app/.venv/bin/gunicorn", "-b", "0.0.0.0:8081", "kiratech.wsgi"]