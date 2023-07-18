FROM python:3.10-alpine
WORKDIR /app

COPY port_state.py .
ENTRYPOINT ["/bin/sh", "-c", "python port_state.py \"$IP\" \"$PORT\" \"$TIMEOUT\""]