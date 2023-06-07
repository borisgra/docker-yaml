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
sudo apt update && sudo apt install nano && sudo apt install -y git #  Install dependencies
sudo git clone https://github.com/borisgra/docker-yaml.git --branch main
sudo chmod 777 docker-yaml/config*
cd docker-yaml/yamls
sudo bash -c "$(cat ../install_docker.sh)"

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
sudo docker images
sudo docker rmi <images>  # remove images (image1 image2 image3 ...)
sudo service docker restart
sudo systemctl stop docker.socket

sudo git stash save # clear last modif in current git

# Dockerfile  (add needed pakets in image)
sudo docker build -t odoo-my:9.0 . # build new image (Dockerfile in current dir)

https://www.baeldung.com/ops/root-user-password-docker-container
sudo docker compose exec -it odoo bash  # NOT root acccess
sudo docker compose exec -it -u root odoo bash  # root acccess

sudo docker compose cp ~/daas_2023-01-23_17-51-22.dump pgadmin:/var/lib/pgadmin/storage/mail_gmail.com

sudo service docker restart
sudo systemctl stop docker.socket
sudo systemctl status docker.service

GCP:
https://stackoverflow.com/questions/67265822/where-are-my-storage-pd-capacity-charges-coming-from 
gcloud compute instances list
gcloud compute zones list
export from VM/Images (not MashinaImages)  !!
gcloud compute images export --destination-uri gs://vpn-gra/images/image-vpn-pgsql-admin4.tar.gz --image image-vpn-pgsql-admin4
gsutil mv -r gs://vpn-gra/images/*  gs://store-gra/images
gsutil cp gs://public-gra/temp/daas_2023-01-23_17-51-22.dump ~

https://rominirani.com/hands-on-guide-to-scheduling-vm-instances-to-start-and-stop-a079a50e16c6 

DELETE !!!
gsutil retention temp release gs://boris-gra-bucket/suplements/Chirka-Kem-08.2016.avi
gsutil -m retention event release gs://boris-gra/images/*.*
gsutil retention temp release gs://boris-gra/images/*.*
</pre>