FROM python:3.12-slim

# Create a non-root user
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chown -R nonroot:nonroot /app

USER nonroot

ENTRYPOINT ["./gunicorn.sh"]
