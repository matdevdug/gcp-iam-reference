FROM python:3.12-slim

# Create a non-root user
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Download pricing.yml and store it in the container
RUN wget https://raw.githubusercontent.com/Cyclenerd/google-cloud-pricing-cost-calculator/master/pricing.yml -O pricing.yml

COPY . .

RUN chown -R nonroot:nonroot /app

USER nonroot

ENTRYPOINT ["./gunicorn.sh"]
