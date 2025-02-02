# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the server code
COPY basic_server.py .

# Expose the server port
EXPOSE 9999

# Command to run the server
CMD ["python", "basic_server.py"]