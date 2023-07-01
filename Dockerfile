# Use the official Python base image with version 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose a port if your application listens on a specific port
# EXPOSE 8000

# Specify the command to run your application
CMD ["python", "app.py"]
