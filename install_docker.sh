#!/bin/bash
sudo apt update && sudo apt install nano && sudo apt install -y git #  Install dependencies
sudo git clone https://github.com/borisgra/docker-yaml.git --branch main
sudo chmod 777 docker-yaml/config*
cd docker-yaml/yamls
sudo bash -c "$(curl -fsSL https://get.docker.com)" #https://docs.docker.com/engine/install/ubuntu/

sudo docker compose up # pgsql:version+pgAdmin4:last+odoo:version  (param in .env)