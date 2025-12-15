#!/bin/bash
sudo apt update
sudo apt install net-tools  # ifconfig
echo "install docker -----------------------"
sudo bash -c "$(curl -fsSL https://get.docker.com)"
echo "installed docker !!! -----------------------"
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/compose-query.yaml -O
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/compose-bd.yaml -O
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/.env_query > .env_query
curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/yamls/.env > .env
sudo mkdir config_pgadmin4
sudo mkdir config_pgadmin4/storage
sudo mkdir config_pgadmin4/storage/mail_gmail.com
sudo chmod 777 -R config*
echo "install certbot , registr SSL"
sudo apt install certbot python3-certbot-nginx -y  # install nginx
sudo certbot --nginx -d boris-gra.xyz -d www.boris-gra.xyz # Obtain and Install SSL
sudo nginx -t && sudo systemctl reload nginx # test and nginx reload
echo "Run query , loadmenu , computers-start-stop"
sudo docker compose -f compose-query.yaml --env-file .env_query up &&
sudo docker compose -f compose-bd.yaml --env-file .env up
