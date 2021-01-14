FROM python:3.9.1 AS python-basic

RUN apt-get update

COPY requirements.dev.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.dev.txt
RUN pip freeze > requirements.dev.txt

COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

FROM python-basic AS builder

# install zh language, results in 13Gb size image
# this creates a file `/cc.zh.300.bin`
RUN python -c "import fasttext.util; fasttext.util.download_model('zh')" && rm /cc.zh.300.bin.gz
