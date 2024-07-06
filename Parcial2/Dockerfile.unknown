FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y \
    ansible iputils-ping \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /etc/ansible/docker3

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

