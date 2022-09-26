FROM python:3.10.4-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN mkdir -p ./logs

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry==1.2.0
RUN poetry config virtualenvs.create false

COPY poetry.lock* pyproject.toml ./
ARG INSTALL_DEV=false
RUN echo Install dev packages: $INSTALL_DEV
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install ; else poetry install --no-dev ; fi"

COPY ./ /app