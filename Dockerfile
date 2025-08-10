# 1. Use an official Python image as the base
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# 3. Set working directory inside container
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project
COPY . /app/

# Collect static files during build
RUN python manage.py collectstatic --noinput

# 6. Expose the port (Django default is 8000)
EXPOSE 8000

# 7. Run migrations and start server
CMD ["gunicorn", "anon.wsgi:application", "--bind", "0.0.0.0:8000"]
