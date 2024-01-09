FROM ubuntu:latest

# Install needed dependencies
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN apt-get -yqq install xfoil

# Copy the application code
COPY . /app
WORKDIR /app

# Get Python dependencies
RUN pip3 install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python3", "./app.py"]