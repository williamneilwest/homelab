# Use a Python image for the backend
FROM python:3.9

# Set the working directory for the backend
WORKDIR /app/backend

# Copy requirements.txt and install Flask
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY backend .

# Copy the built Vite files from the host into the container
COPY ./frontend/dist ./frontend

# Set the environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the necessary port for Flask
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8445"]