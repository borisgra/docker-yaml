FROM python:3.12-slim as version
RUN apt-get update && apt-get install -y git

ARG GIT="https://github.com/borisgra/docker-yaml.git"
ENV GIT=$GIT
ARG BRANCH="main"
ENV BRANCH=$BRANCH

#ADD "https://currentmillis.com/time/minutes-since-unix-epoch.php" skipcache

WORKDIR /app-cashed/cloud-start-stop
ADD https://raw.githubusercontent.com/borisgra/docker-yaml/refs/heads/$BRANCH/cloud-start-stop/requirements.txt /app-cashed/cloud-start-stop
RUN pip install -r requirements.txt

#https://stackoverflow.com/questions/35134713/disable-cache-for-specific-run-commands
#ADD "https://currentmillis.com/time/minutes-since-unix-epoch.php" skipcache
ADD https://api.github.com/repos/borisgra/docker-yaml/git/refs/heads/$BRANCH version.json

RUN git clone --single-branch --branch $BRANCH $GIT /app

WORKDIR /app

RUN git rev-list --first-parent --count HEAD > ver  && \
    git rev-parse --verify --short HEAD >> ver && \
    echo $(date '+%Y-%m-%d %H:%M:%S') >> ver

FROM python:3.12-slim

COPY --from=version /app/cloud-start-stop /app
COPY --from=version /app/ver /
COPY --from=version /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

WORKDIR /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["cloudrun.py"]

# sudo docker image build  --progress=plain -t borisgra/vm:latest . 2>&1 | tee build.log
# sudo docker image build --no-cache -t borisgra/vm:latest .
# sudo docker login -u borisgra
# sudo docker push borisgra/vm:latest
# sudo docker pull borisgra/vm:latest
# sudo docker run borisgra/vm:latest -p 5004:5004
# docker builder prune  # clear cache