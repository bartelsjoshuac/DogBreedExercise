# Don't use -slim as it has issues
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Probably a could do this more dynically with the pip freeze.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

### Removed since we are doing it in the docker-compose file in a cmd
#EXPOSE 8000

### Removed since we are doing it in the docker-compose file in a cmd
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]