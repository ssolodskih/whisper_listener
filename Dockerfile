FROM python:3.11-slim

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir /app && \
    apt-get update && \
    apt-get install -y git curl wget libpq-dev python-dev-is-python3 gcc build-essential libssl-dev cmake sox ffmpeg openssl libssl-dev portaudio19-dev python3-pyaudio

RUN pip install pipx
RUN pipx install "poetry"
RUN pipx ensurepath

COPY poetry.lock pyproject.toml /app/
RUN cd /app/ && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /app

WORKDIR /app/src

CMD python3 main.py
