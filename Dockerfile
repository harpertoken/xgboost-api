FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code and model
COPY app.py .
COPY model/xgboost_model.json model/

# Set environment variable for GPU support
ENV CUDA_VISIBLE_DEVICES=0

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python3", "app.py"]
