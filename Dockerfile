# Use an official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy app files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]