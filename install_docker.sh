#!/bin/bash
echo "Install dependencies --------------------"
sudo apt update && sudo apt install nano && sudo apt install -y git
sudo apt install net-tools # ifconfig ( first ip address for inner connects and third for putty )
sudo apt remove openssh-server && sudo apt install openssh-server && sudo service ssh start  # for Ubuntu, Debian on Window
sudo git clone https://github.com/borisgra/docker-yaml.git --branch main
sudo chmod 777 docker-yaml/config*
cd docker-yaml/yamls

echo "install docker -----------------------"
sudo bash -c "$(curl -fsSL https://get.docker.com)"
echo "installed docker !!! -----------------------"
sudo service docker start # for Ubuntu-20.04 , Debian on Window
echo "install pgsql:version+pgAdmin4:version+odoo:version  (version in .env) "
sudo docker compose up