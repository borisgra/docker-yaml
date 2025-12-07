#!/bin/bash
sudo apt update
sudo apt install net-tools  # ifconfig
echo "install docker -----------------------"
sudo bash -c "$(curl -fsSL https://get.docker.com)"
echo "installed docker !!! -----------------------"
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/compose-query.yaml -O
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/compose-bd.yaml -O
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/.env_query > .env_query
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/.env - O
sudo mkdir config_pgadmin4
sudo chmod 777 config*
echo "install query , loadmenu , computers-start-stop"
sudo docker compose -f compose-query.yaml --env-file .env_query up
#sudo docker compose -f compose-bd.yaml --env-file .env up