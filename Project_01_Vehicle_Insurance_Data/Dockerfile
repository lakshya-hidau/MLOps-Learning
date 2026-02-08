# Use an official Python 3.11.5 image from Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Add ENV PYTHONUNBUFFERED=1 to avoid buffering issues with Python output in Docker
ENV PYTHONUNBUFFERED=1

# Install system dependencies (optional but recommended)
RUN apt-get update && apt-get install -y \
build-essential \
&& rm -rf /var/lib/apt/lists/*

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install any necessary dependencies (if you have a requirements.txt file)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Hugging Face Spaces requires port 7860
EXPOSE 7860

# Run the app
# CMD ["python", "app.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
