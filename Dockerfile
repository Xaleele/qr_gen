# Use official Python runtime as base image
FROM python:3.9

Run apt-get update && \
    apt-get install -y \
    xvfb \
    xauth \
    x11-xserver-utils \
    tk

# Set working directory inside the container
WORKDIR /app

# Copy Python requirements file into the container
COPY requirements.txt .

# Install Python dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point script for X11 forwarding
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy Python script into container
COPY qr_gen.py .

# Set command to run qr generator script
CMD ["/entrypoint.sh"]