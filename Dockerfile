FROM python:3.9.1 AS python-basic

RUN apt-get update

COPY requirements.dev.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.dev.txt
RUN pip freeze > requirements.dev.txt

COPY src/ /app/src
COPY data/ /app/data
COPY app.py /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

FROM python-basic AS builder

# hack to optionally copy the fasttext bin file
# and skip the following download step
# .gitignore is needed so that cc.zh.300.bin is optional 
COPY .gitignore cc.zh.300.bin* /

# install zh language, results in 13Gb size image
# this creates a file `/cc.zh.300.bin`
RUN python -c "import fasttext.util; fasttext.util.download_model('zh')" && rm -f /cc.zh.300.bin.gz
