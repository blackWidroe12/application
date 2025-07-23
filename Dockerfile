FROM python:3.11

# Install system dependencies for GDAL and PostGIS
RUN apt-get update && \
    apt-get install -y \
    binutils \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set GDAL environment variables
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000