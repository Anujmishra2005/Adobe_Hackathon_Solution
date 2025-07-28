# Base Image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set entrypoint
CMD ["python", "main.py"]
