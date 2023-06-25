#!/bin/bash
echo "Install dependencies --------------------"
sudo apt update && sudo apt install nano && sudo apt install -y git
sudo apt install net-tools # ifconfig ( if WSL Windows: first ip address for inner connects and third for putty )
sudo git clone https://github.com/borisgra/docker-yaml.git --branch main
sudo chmod 777 docker-yaml/config*
cd docker-yaml/yamls

echo "install docker -----------------------"
sudo bash -c "$(curl -fsSL https://get.docker.com)"
echo "installed docker !!! -----------------------"
echo "install pgsql:version+pgAdmin4:version+odoo:version  (version in .env) "
sudo docker compose up