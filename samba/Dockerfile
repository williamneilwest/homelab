# Use an official Node.js runtime as the base image for the frontend
FROM node:16 AS frontend

# Set the working directory for the frontends
WORKDIR /app/frontend

# Copy the frontend package and install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy the frontend code
COPY frontend/ ./

# Build the React app
RUN npm run build

# Now, for the Flask backend, use Python
FROM python:3.9 AS backend

# Set the working directory for the backend
WORKDIR /app/backend

# Copy the backend requirements and install dependencies
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

# Copy the backend code
COPY backend/ ./

# Expose the necessary ports
EXPOSE 80

# Set the default command to run both the Flask app and the React app
CMD ["sh", "-c", "flask run --host=0.0.0.0 & serve -s /app/frontend/dist -l 80"]
