FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (Docker layer caching — if requirements.txt
# doesn't change, this layer is reused on rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]