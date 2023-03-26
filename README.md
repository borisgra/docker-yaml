<H3> Install docker with odoo 16,15,14 and other ver. , pgsql , pgadmin4</H3> 
<div style="color:Red;"><b>Attention!!! When create odoo base - base name needed start with odooXX (XX - ODOO_VERSION)  or change dbfilter in odoo.conf   </b></div>
<pre>
VM instances (min):
system disk- 10G for 1 odoo, 20G for several one (Ubuntu min)
procesor 1
memory min 1.7G
open ports in firewall ( gcloud compute firewall-rules create my-odoo-rule --allow tcp:5010,tcp:10010-10020 --source-ranges=0.0.0.0/0  
</pre>
<pre>
##curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh  # version install docker 1 (https://gist.github.com/zulhfreelancer/254c4a157c586dd232c1a51db0f6eac3)
sudo apt-get install nano
sudo apt-get install -y git
sudo bash -c "$(cat install_docker.sh)" # version install docker 2
git init
sudo git pull https://github.com/borisgra/docker-yaml.git
cd ~/yamls

sudo docker compose up # pgsql:version+pgAdmin4:last+odoo:version  (param in .env)
By default ODOO_VERSION=16 (in .env),If needed, change ODOO_VERSION :
1) sudo docker compose stop
2) sudo nano .env # change ODOO_VERSION  (for ODOO_VERSION<13 - POSTGRES_VERSION)
3) sudo docker compose up # pgsql:version+pgAdmin4:last+odoo:version  # version in file .env  (13.10+last+11)

sudo docker compose stop
sudo docker compose start 


sudo docker compose down 
sudo docker compose -f compose.yaml -f compose-odoo-14-15-16.yaml up # pgsql:13.10+pgAdmin4:last+odoo:16+15+14+11
sudo docker compose -f compose-bd.yaml up # pgsql:version+pgAdmin4:last
sudo docker compose -f compose-odoo-ver.yaml up # odoo:ver
sudo docker compose -f compose-odoo-old.yaml up # ODOO_VERSION_OLD=

sudo docker compose restart odoo # restart service
sudo docker compose down  # delete all containers
sudo docker compose down --remove-orphans # if error: while removing network: network yamls_default
sudo docker container stop odoo
sudo docker container rm odoo
sudo service docker restart
sudo systemctl stop docker.socket

sudo git stash save # clear last modif in current git
</pre>