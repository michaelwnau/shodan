# Use the official Python base image with version 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . /app

# Expose a port if your application listens on a specific port
# EXPOSE 8000

# Specify the command to run your application
CMD ["python", "main.py"]
