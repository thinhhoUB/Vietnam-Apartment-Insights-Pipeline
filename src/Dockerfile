# Use the official Python base image with ARM64 support
FROM python:3.9-slim-buster

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-cache policy google-chrome-stable && \ 
    apt-get install -y chromium && \
    rm -rf /var/lib/apt/lists/*

# Set an environment variable
ENV CHROME_BIN=/usr/bin/chromium-browser

# Install Python dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Python script
CMD ["python", "web_scrapping.py"]