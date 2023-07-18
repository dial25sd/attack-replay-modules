FROM python:3.10-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY check_endpoints.py .
ENTRYPOINT ["/bin/sh", "-c", "python check_endpoints.py \"$PROTOCOL\" \"$HOST\" \"$PORT\" \"$METHOD\" \"$TIMEOUT\" $ENDPOINTS"]