FROM ubuntu:latest

# Install needed dependencies
RUN apt-get update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN apt-get -yqq install xfoil

# Copy the application code
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Get the requirements for the Xfoil package
# RUN apt install -yqq /app/dependencies/libquadmath0.deb
# RUN apt install -yqq /app/dependencies/libgfortran5.deb
# RUN apt install -yqq /app/dependencies/libxcb1.deb
# RUN apt install -yqq /app/dependencies/libx11-data.deb
# RUN apt install -yqq /app/dependencies/libxau6.deb
# RUN apt install -yqq /app/dependencies/libxdmcp6.deb
# RUN apt install -yqq /app/dependencies/libx11-6.deb

# RUN apt install -yqq /app/dependencies/xfoil.deb

# Get Python dependencies
RUN pip3 install -r requirements.txt

COPY . /app

ENV PYTHONPATH="${PYTHONPATH}:/app/Airfoils"

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python3", "app.py"]