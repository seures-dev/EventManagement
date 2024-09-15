
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /API


COPY requirements.txt /API/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /API/

RUN python3 EventManager/manage.py makemigrations

RUN python3 EventManager/manage.py migrate

EXPOSE 8000


CMD ["python3", "./EventManager/manage.py", "runserver", "0.0.0.0:8000"]
