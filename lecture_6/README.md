# FastAPI Docker App

## Description
Simple FastAPI application with `/healthcheck` endpoint, containerized using Docker.

## Run locally with Docker
```bash
docker build -t app:latest .
docker run -p 8000:8000 app:latest
