FROM python:3.10-alpine
WORKDIR /app

RUN apk add --no-cache nmap nmap-scripts
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service_fingerprinting.py .
ENTRYPOINT ["/bin/sh", "-c", "python service_fingerprinting.py \"$IP\" \"$PORT\""]