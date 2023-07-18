FROM python:3.10-alpine
WORKDIR /app

RUN apk add --no-cache nmap nmap-scripts
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scanner_service_port.py .
ENTRYPOINT ["/bin/sh", "-c", "python scanner_service_port.py \"$IP\" \"$SERVICE_NAME\""]