FROM python:3.9.1

RUN apt-get update

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app"