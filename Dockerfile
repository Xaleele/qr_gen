# Use official Python runtime as base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy Python requirements file into the container
COPY requirements.txt .

# Install Python dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python script into container
COPY qr_gen.py .

# Set command to run qr generator script
CMD ["python","qr_gen.py"]