### Base stage
FROM python:3.11-bullseye as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.3.2

WORKDIR /app

### Dev stage
FROM base as dev

ENV PYTHONDONTWRITEBYTECODE=true \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100


# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

# Creating folders, and files for a project:
COPY . .

EXPOSE 8080

### Prod stage
FROM base as prod
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 

COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false && \
    poetry install --without dev --no-root

COPY . .

EXPOSE 8080