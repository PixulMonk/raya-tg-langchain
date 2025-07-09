FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy code into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "app.py"]
