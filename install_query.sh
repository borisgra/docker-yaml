#!/bin/bash
echo "install docker -----------------------"
sudo bash -c "$(curl -fsSL https://get.docker.com)"
echo "installed docker !!! -----------------------"
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/compose-query.yaml -O
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/.env_query > .env
echo "install query , loadmenu , computers-start-stop"
sudo docker compose -f compose-query.yaml up