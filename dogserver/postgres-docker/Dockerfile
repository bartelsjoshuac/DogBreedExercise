# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set environment variables for Postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
#ENV POSTGRES_DB=dogserver
ENV POSTGRES_DB=dogserverdb

# Copy any custom initialization SQL or scripts
#COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432