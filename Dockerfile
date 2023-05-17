# Use official Python runtime as base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy Python requirements file into the container
COPY requirements.txt .

# Install Python dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Set the secret key environment variable
ENV SECRET_KEY=projects/876748653486/secrets/quokka-secrets 

# Copy the Flask application files into container
COPY qr_gen_flask.py .
COPY templates templates

# Expose a port for the Flask application to run on
EXPOSE 8080

# Set command to run qr generator script
CMD ["python", "qr_gen_flask.py"]