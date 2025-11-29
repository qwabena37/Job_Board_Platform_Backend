# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files into container
COPY . /app/

# Collect static files (optional, if you have static files)
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server (change to gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
