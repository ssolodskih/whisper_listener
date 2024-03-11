FROM python:3.11-slim

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir /app && \
    apt-get update && \
    apt-get install -y git curl wget libpq-dev python-dev gcc build-essential libssl-dev cmake sox ffmpeg

RUN curl -sSL https://install.python-poetry.org | python3
RUN poetry self update 1.8.2

COPY poetry.lock pyproject.toml /app/
RUN cd /app/ && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /app

WORKDIR /app/src

CMD python main.py
