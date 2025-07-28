# Use a lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy solution directories
COPY Solution_1a/ Solution_1a/
COPY Solution_1b/ Solution_1b/

# Copy and merge requirements
COPY Solution_1a/requirements.txt Solution_1a_requirements.txt
COPY Solution_1b/requirements.txt Solution_1b_requirements.txt

# Combine, deduplicate and install requirements
RUN cat Solution_1a_requirements.txt Solution_1b_requirements.txt | sort -u > requirements.txt && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm Solution_1a_requirements.txt Solution_1b_requirements.txt

# Default command
CMD [ "python3" ]
