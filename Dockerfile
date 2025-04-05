# Using an official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port that the app runs on
EXPOSE 5000cl

# Command to run the app
CMD ["python", "app.py"]