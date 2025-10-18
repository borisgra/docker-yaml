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
# install docker and start  pgsql:version+pgAdmin4:version+odoo:version  (version in .env file)
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/main/install_docker.sh)"

By default ODOO_VERSION=16 (in .env),If needed, change ODOO_VERSION :
1) sudo docker compose down
2) sudo nano .env # change ODOO_VERSION  (for ODOO_VERSION<10 - POSTGRES_VERSION < 14)
3) sudo docker compose up 

sudo docker compose stop
sudo docker compose start 


sudo docker compose down 
sudo docker compose -f compose-hook.yaml # with webhook (before start: sh create_service.sh)
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

sudo git clone https://github.com/mmodrive/OdooX_Addons.git ~/docker-yaml/config_X/addons     # load addons

# Dockerfile  (add needed package in image)
sudo docker build -t odoo:9.0 . #   replase odoo:9.0 build new image (Dockerfile in current dir)

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
export from VM/Images: (not MashinaImages)  !!
gcloud compute images export --destination-uri gs://vpn-gra/images/image-vpn-pgsql-admin4.tar.gz --image image-vpn-pgsql-admin4
gsutil mv -r gs://vpn-gra/images/*  gs://store-gra/images
gsutil cp gs://public-gra/temp/daas_2023-01-23_17-51-22.dump ~

win10-intellij import (replace com-gra on real project):
Go to progect com-gra and create images and instance ($50 month or $0.07 hourly)   ~ 7min:
gcloud compute images create win10-intellij --source-uri=gs://store-gra/images/win10-intellij.tar.gz --project=com-gra --storage-location=us-central1
gcloud compute images create win10-intellij-data --source-uri=gs://store-gra/images/win10-intellij-data.tar.gz --project=com-gra --storage-location=us-central1

gcloud compute instances create win10-intellij \
--project=com-gra \
--zone=us-central1-a \
--machine-type=e2-standard-2 \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append \
--create-disk=auto-delete=no,boot=yes,device-name=win10-intellij,image=projects/com-gra/global/images/win10-intellij,mode=rw,size=25,type=pd-standard \
--create-disk=device-name=win10-intellij-data,image=projects/com-gra/global/images/win10-intellij-data,mode=rw,name=win10-intellij-data,size=10,type=pd-standard \
--labels=goog-ec-src=vm_add-gcloud \
--reservation-affinity=any 

connect by windows Remote Deckstop
    ip - External IP VM Instance (Compute Engine VM instances)
    The default username and password are set to user/123456

unzip on D:  d:\distrib\mde-partision-free-portable.zip

For service instance start/stop https://comps-907412932172.us-central1.run.app/?projects=com-gra,vpn-gra,gke-gra :
https://console.cloud.google.com/iam-admin/roles?project=vpn-gra
create new role "Custom ComputeStartStop" with permision:
compute.instances.list	
compute.instances.start	
compute.instances.stop	

https://console.cloud.google.com/iam-admin/iam?project=vpn-gra (View by principals + Grant access)
Add to project vpn-gra principal "myserviceaccount@vpn-gra.iam.gserviceaccount.com" 
with role "Custom ComputeStartStop" 

Moove Users to anothe disk
https://www.top-password.com/blog/move-the-entire-user-profiles-to-another-drive-in-windows/
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

win10-gcp (https://www.youtube.com/watch?v=DcUA_S2n7Qw&list=WL&index=1):
gcloud compute instances create win10-create \
--project=com-gra \
--zone=us-central1-a \
--machine-type=e2-medium \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--metadata=enable-osconfig=TRUE \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--create-disk=auto-delete=yes,boot=yes,device-name=win10-create,image=projects/debian-cloud/global/images/debian-12-bookworm-v20251014,mode=rw,size=10,type=pd-balanced \
--create-disk=auto-delete=no,device-name=win10,mode=rw,name=win10,size=25,type=pd-standard 

# !!! wait 30 sec while starting instance
gcloud compute ssh --project=com-gra --zone=us-central1-a win10-create # start console VM  
sudo bash -c "$(curl -fsSL https://storage.googleapis.com/public-gra/images/win10-gcp/win.sh)" # execute (~5min  on e2-medium)
#sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/win.sh)" # execute (~5min  on e2-medium)

exit
gcloud compute instances delete win10-create --zone=us-central1-a 
# !!! wait 30 sec while delete instance
gcloud compute instances create win10 \
--project=com-gra \
--zone=us-central1-a \
--machine-type=e2-standard-2 \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--metadata=enable-osconfig=TRUE \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--disk=boot=yes,device-name=win10,mode=rw,name=win10 \
--create-disk=auto-delete=no,device-name=win10-data,mode=rw,name=win10-data,size=10,type=pd-standard 

load and unzip https://storage.googleapis.com/public-gra/images/win10-gcp/distrib_for_win10GCP.zip
if you will copy c:/Users to d: use teracopy-portable.exe from distrib_for_win10GCP
  and correct path in  regedit HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList
  and all users (starting with ‘S-1-5-‘)


WSL (Windows Subsystem for Linux):  Unix on Windows
install wsl in cmd: dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --export --vhd Ubuntu-24.04 F:/temp/WpSystem-my/Ubuntu-24.04/ext4.vhdx
wsl --import-in-place ubuntu_24.04docker F:\temp\WpSystem-my\Ubuntu-24.04\ext4.vhdx
wsl --manage ubuntu_24.04docker --set-sparse true

https://learn.microsoft.com/ru-ru/windows/wsl/basic-commands#import-a-distribution
DELETE !!!
gsutil -m retention event release gs://boris-gra/images/*.*
gsutil retention temp release gs://boris-gra/images/*.*
</pre>