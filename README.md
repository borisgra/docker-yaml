<H4># Install docker https://gist.github.com/zulhfreelancer/254c4a157c586dd232c1a51db0f6eac3
<div style="color:Red;"><b>Attention!!! When create odoo base - base name needed start with odooXX (XX - ODOO_VERSION)  or change dbfilter in odoo.conf   </b></div>
<pre>
VM instances (min):
system disk- 10G for 1 odoo, 20G for several one (Ubuntu min)
procesor 1
memory min 1.7G
open ports in firewall ( gcloud compute firewall-rules create my-odoo-rule --allow tcp:5010,10010-10020 --source-ranges=0.0.0.0/0  
</pre>
<pre>
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo apt-get install nano
sudo apt-get install unzip # unzip view_models.zip
git init
sudo git pull https://github.com/borisgra/docker-yaml.git
cd yamls

sudo docker compose up # pgsql:version+pgAdmin4:last+odoo:version  (param in .env)
By default ODOO_VERSION=16 (in .env),If needed, change ODOO_VERSION :
1) sudo docker compose stop
2) sudo nano .env # change ODOO_VERSION  (for ODOO_VERSION<13 - POSTGRES_VERSION)
3) sudo docker compose up 

sudo docker compose stop
sudo docker compose start
sudo docker compose -f compose-bd.yaml -f compose-odoo-all.yaml up # pgsql:version+pgAdmin4:last+odoo:16+15+14
sudo docker compose -f compose-odoo-all.yaml up # odoo:16+15+14
sudo docker compose -f compose-bd.yaml up # pgsql:version+pgAdmin4:last
sudo docker compose -f compose-odoo-ver.yaml up # odoo:ver

sudo docker compose restart odoo # restart service
sudo docker compose down  # delete all containers
sudo docker compose down --remove-orphans # if error: while removing network: network yamls_default
sudo docker container stop odoo
sudo docker container rm odoo
sudo service docker restart
sudo systemctl stop docker.socket

sudo git stash save # clear last modif in current git
</pre>