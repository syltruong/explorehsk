FROM python:3.9.1 AS basic

RUN apt-get update

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ /app/src
COPY data/ /app/data
COPY app.py /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

## Extra steps to install the `zh` fasttext model
## for model building and dumping
FROM basic AS builder

COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# hack to optionally copy the fasttext bin file
# and skip the following download step
# put `cc.zh.300.bin` to skip the next step
COPY Dockerfile cc.zh.300.bin* /

# install zh language, results in 13Gb size image
# this creates a file `/cc.zh.300.bin`
RUN python -c "import fasttext.util; fasttext.util.download_model('zh')" && rm -f /cc.zh.300.bin.gz
