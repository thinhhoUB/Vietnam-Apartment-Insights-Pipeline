# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Update package lists and install required packages
RUN apt-get update && apt-get install -y wget gnupg

# Download and add Google Chrome signing key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add Google Chrome repository to apt sources list
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update package lists again
RUN apt-get update

# Install Google Chrome stable
RUN apt-get install -y google-chrome-stable

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your Python script
CMD ["python", "web_scrapping.py"]
