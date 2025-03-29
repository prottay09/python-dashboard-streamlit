FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

CMD [ "streamlit", "run", "src/app.py", "--host", "0.0.0.0", "--port", "8080"]