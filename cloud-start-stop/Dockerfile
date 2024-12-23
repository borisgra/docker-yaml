FROM python:3.12-slim as version
RUN apt-get update && apt-get install -y git

ARG GIT="https://borisgra@github.com/borisgra/docker-yaml.git"
ENV GIT=$GIT

RUN git clone --single-branch --branch develop $GIT /app # --no-cache  --progress=plain

WORKDIR /app

RUN git rev-list --first-parent --count HEAD > ver  && \
    git rev-parse --verify --short HEAD >> ver && \
    echo $(date '+%Y-%m-%d %H:%M:%S') >> ver

FROM python:3.12-slim

COPY --from=version /app/cloud-start-stop /app
COPY --from=version /app/ver /

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["cloudrun.py"]
