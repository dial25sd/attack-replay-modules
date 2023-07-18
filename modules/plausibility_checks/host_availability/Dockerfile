FROM python:3.10-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY host_ping.py .
ENTRYPOINT ["/bin/sh", "-c", "python host_ping.py \"$IP\" \"$TIMEOUT\""]