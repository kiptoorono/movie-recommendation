FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies individually
RUN pip install --no-cache-dir flask pandas numpy scikit-learn celery redis requests psutil

# Expose the port Flask app will run on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
