# Use a minimal base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Drop privileges to non-root user
USER appuser

# Add a basic health check (e.g., ping the root endpoint)
HEALTHCHECK --interval=30s --timeout=3s CMD wget --spider -q http://localhost:5000/ || exit 1

# Run the app
CMD ["python", "app.py"]

