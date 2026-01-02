<pre>
#  sudo su -c /usr/lib/openssh/sftp-server  # for winSCP (edit/edvanset/SFTP) (debian sudo apt install openssh-server)
# sudo ifconfig
# ss -tulpn | grep LISTEN   # open ports
# sudo passwd root
# sudo shutdown -h nov

VM instances (min):
system disk- 10G  - Debian /Ubuntu
procesor 1 memory min 1G  (N2 type - custom-1-1024 - 0.035 usd/h)
open ports in firewall ( gcloud compute firewall-rules create my-rule --allow tcp:5003,3000,8080 --source-ranges=0.0.0.0/0

install docker and start  install query , loadmenu , computers-start-stop
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/develop/install_query.sh)"
</pre>
<H3> Install docker with odoo 16,15,14 and other ver. , pgsql , pgadmin4</H3> 
<div style="color:Red;"><b>Attention!!! When create odoo base - base name needed start with odooXX (XX - ODOO_VERSION)  or change dbfilter in odoo.conf   </b></div>
<pre>
VM instances (min):
system disk- 10G for 1 odoo, 20G for several one (Ubuntu min)
procesor 1 memory min 1.7G
open ports in firewall ( gcloud compute firewall-rules create my-odoo-rule --allow tcp:5010,tcp:10010-10020 --source-ranges=0.0.0.0/0
# install docker and start  pgsql:version+pgAdmin4:version+odoo:version  (version in .env file)
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/borisgra/docker-yaml/main/install_docker.sh)"
</pre>
<pre>
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
https://cloud.google.com/storage/pricing?hl=ru
gcloud storage objects update gs://public-gra/images/** --storage-class=COLDLINE # STANDARD -> NEARLINE -> COLDLINE -> ARHIVE 
export from VM/Images: (not MashinaImages)  !!
gcloud compute images export --destination-uri gs://vpn-gra/images/image-vpn-pgsql-admin4.tar.gz --image image-vpn-pgsql-admin4
gsutil mv -r gs://vpn-gra/images/*  gs://store-gra/images
gsutil cp gs://public-gra/temp/daas_2023-01-23_17-51-22.dump ~
gsutil du -ach gs://com-gra
gsutil du -ach gs://*     # all bucket in current project
gsutil du -sh gs://*     # summ by bucket
gsutil -m  rm -r  gs://*   # delete all bucket in current project
gsutil -m  mv -r  gs://*   # move all bucket from current project
gsutil -m  cp -r  gs://*   # copy all bucket from current project
gcloud config get-value project
gcloud config set project new-project
gcloud help
curl https://raw.githubusercontent.com/borisgra/menus/refs/heads/main/menu-koyeb.js | gsutil cp - gs://gke-gra
gcloud storage buckets update gs://my-bucket --soft-delete-duration=1d  # 0d - cancel  
curl https://storage.googleapis.com/store-gra/public-gra/images/win10-gcp/windows-10-ggcloud.raw.gz | aws s3 cp - s3://aws-strore-gra/win10/windows-10-ggcloud.raw.gz
curl https://aws-strore-gra.s3.us-east-1.amazonaws.com/win10/win.sh  | aws s3 cp - s3://aws-strore-gra/win10/win-3.sh
# not work ??
gcloud transfer jobs create \
gs://public-gra/rednoise/rednoise_alfa.apk/ \
s3://aws-strore-gra/win10/ / \
--include-prefixes=prefix --immediate

# all bucket in ALL project
for project in $(gcloud projects list --format="value(projectId)"); do
        echo "Project: $project"
        gcloud config set project "$project" >/dev/null
        for bucket in $(gsutil ls); do
            echo "Bucket: $bucket"
            gsutil du -ach $bucket
        done
    done
gcloud config set project store-gra

https://console.cloud.google.com/iam-admin/iam?project=store-gra # (View by principals + Grant access)
Add to project store-gra principal :
       "148641556397-compute@developer.gserviceaccount.com"   # gke-gra
   and "878732527619-compute@developer.gserviceaccount.com"   # com-gra
   and "907412932172-compute@developer.gserviceaccount.com"   # vpn-gra
with role "Storage Admin"

gcloud compute images export --destination-uri gs://store-gra/images/image-1.tar.gz --image image-1

Debian/Ubuntu:
f1-micro 0.25-1 vCPU (1 shared core) 614 MB  0.025 ? usd/h
g1-small 0.5-1 vCPU (1 shared core) 1.7 GB   0.03 usd/h ?
e2-micro (2 vCPU, 1 core, 1 GB memory)  0.01 usd/h
e2-small (2 vCPU, 1 core, 2 GB memory)  0.03 usd/h
N2 type - custom-1-1024 - 0.035 usd/h
Set ssh key for All instances
https://console.cloud.google.com/compute/metadata?project=com-gra&scopeTab=projectMetadata&resourceTab=sshkeys
 or
gcloud compute project-info add-metadata \
--metadata-from-file ssh-keys=root-pub
export ssh key:
gcloud compute project-info describe \
--format="value(commonInstanceMetadata.items.ssh-keys)" > existing-keys.txt

# myserviceaccount@com-gra.iam.gserviceaccount.com
gcloud iam service-accounts create myserviceaccount \
--description="DESCRIPTION" \
--display-name="myServiceaccount"
or
gcloud projects add-iam-policy-binding com-gra \
--member="serviceAccount:myserviceaccount@com-gra.iam.gserviceaccount.com" \
--role="Custom ComputeStartStop"

gcloud compute instances create debian \
--project=com-gra \
--zone=us-central1-a \
--machine-type=e2-micro \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--metadata=enable-osconfig=TRUE \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--service-account=myserviceaccount@com-gra.iam.gserviceaccount.com
--create-disk=auto-delete=yes,boot=yes,device-name=debian,image=projects/debian-cloud/global/images/debian-13-trixie-v20251014,mode=rw,size=10,type=pd-standard

Add to projects vpn-gra,store-gra,gke-gra principal "myserviceaccount@com-gra.iam.gserviceaccount.com"
with role "Custom ComputeStartStop"
https://console.cloud.google.com/iam-admin/roles?project=vpn-gra

extend file system on 1G :
GCP Manage disk(edit) - set new value
lsblk
df -h
sudo apt install cloud-guest-utils
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1 #EXT4
or
sudo xfs_growfs /  #XFS
df -h

win10min create instance:
curl -s https://raw.githubusercontent.com/borisgra/docker-yaml/develop/win10gcp.sh | \
  bash -s -- -n win10gcp -dt pd-balanced

# images - 6min  5.9G
#--source-uri=https://storage.googleapis.com/public-gra/images/image-gcp-win10-user-123456.tar.gz \
gcloud compute images create win10-user-123456 \
--source-uri=gs://store-gra/images/image-gcp-win10-user-123456.tar.gz \
--project=com-gra \
--storage-location=us-central1

# disk type (25gb): pd-standard=1$ / pd-balanced=2.5$ / pd-ssd=4.25$
#  1 min
# !!! not connected !!!
gcloud compute instances create win10-user-123456 \
--project=com-gra \
--zone=us-central1-a \
--machine-type=e2-standard-2 \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--create-disk=auto-delete=yes,boot=yes,device-name=win10-user-123456,image=projects/com-gra/global/images/win10-user-123456,mode=rw,\
size=25,type=pd-ssd

# delete win10 image 
gcloud compute images delete win10-user-123456 \
--project=com-gra

win10-intellij (two disks):
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
https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances
https://console.cloud.google.com/iam-admin/roles?project=vpn-gra
create new role "Custom ComputeStartStop" with permision:
compute.instances.list	
compute.instances.start	
compute.instances.stop	
compute.instances.reset	

https://console.cloud.google.com/iam-admin/iam?project=????? (View by principals + Grant access)
Add to project ?????? principal "myserviceaccount@?????.iam.gserviceaccount.com" 
with role "Custom ComputeStartStop" 

Moove Users to anothe disk
https://www.top-password.com/blog/move-the-entire-user-profiles-to-another-drive-in-windows/
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

win10-gcp (https://www.youtube.com/watch?v=DcUA_S2n7Qw&list=WL&index=1):
gcloud compute instances create win10-create \
--project=com-gra \
--zone=us-central1-a \
--machine-type=g1-small \
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

AWS

# run-instance win10-create (debian 13 (20251006-2257)) for create disk win10
aws ec2 run-instances --image-id 'ami-0f9c27b471bdcd702' \
--instance-type 't3.micro' \
--key-name 'aws-my' \
--block-device-mappings '{"DeviceName":"/dev/xvda","Ebs":{"Encrypted":false,"DeleteOnTermination":true,"Iops":3000,"SnapshotId":"snap-0c7a56286941e0491","VolumeSize":10,"VolumeType":"gp3","Throughput":125}}' \
  '{"DeviceName":"/dev/sdb","Ebs":{"Encrypted":false,"DeleteOnTermination":false,"Iops":3000,"VolumeSize":25,"VolumeType":"gp3","Throughput":125}}' \
--network-interfaces '{"AssociatePublicIpAddress":true,"DeviceIndex":0,"Groups":["sg-04fee8d3060faa648"]}' \
--credit-specification '{"CpuCredits":"unlimited"}' \
--tag-specifications '{"ResourceType":"instance","Tags":[{"Key":"Name","Value":"win10-create"}]}' \
--metadata-options '{"HttpEndpoint":"enabled","HttpPutResponseHopLimit":2,"HttpTokens":"required"}' \
--private-dns-name-options '{"HostnameType":"ip-name","EnableResourceNameDnsARecord":true,"EnableResourceNameDnsAAAARecord":false}' \
--count '1'

# connect to win10-create
wget -qO- https://raw.githubusercontent.com/ngxson/public-assets/main/install-windows-gcp.sh | sudo bash

# Terminate instance win10-create !!!

# snapshot
aws ec2 create-snapshot \
--volume-id vol-0354d153fe71a26d7 \
--description "Snapshot win10"

# image from SnapshotId
aws ec2 register-image \
--name "My-win10" \
--architecture x86_64 \
--root-device-name /dev/sda1 \
--block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"SnapshotId":"snap-0c5863c4fb155ffae"}}]' \
--virtualization-type hvm

# lunch instance win10 (image above) -- !!! not connected !!!
aws ec2 run-instances --image-id 'ami-03e612d0230414d91' \
--instance-type 't2.large' \
--key-name 'aws-my' \
--network-interfaces '{"AssociatePublicIpAddress":true,"DeviceIndex":0,"Groups":["sg-04fee8d3060faa648"]}' \
--credit-specification '{"CpuCredits":"standard"}' \
--tag-specifications '{"ResourceType":"instance","Tags":[{"Key":"Name","Value":"win10"}]}' \
--private-dns-name-options '{"HostnameType":"ip-name","EnableResourceNameDnsARecord":true,"EnableResourceNameDnsAAAARecord":false}' \
--count '1'

aws ec2 import-image \
--description "My Imported VM Image" \
--disk-containers "Format=<Your_Format>,UserBucket={S3Bucket=<Your_Bucket_Name>,S3Key=<Your_S3_Key_Path>}"

aws ec2 import-image \
--description "My Public S3 Image" \
--disk-containers "Format=<Your_Format>,Url=<S3_HTTPS_or_S3_URL>"

# not work normal (write file  .raw on local) !!?
aws s3 cp s3://aws-strore-gra/images/images_image-gcp-win10-user-123456.tar.gz -   |\
tar -xzOvf -   | \
aws s3 cp - s3://aws-strore-gra/win10/images/gcp-win10.vmdk

WSL (Windows Subsystem for Linux):  Unix on Windows
install wsl in cmd  (Admin):
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
or
wsl --install

wsl --export --vhd Ubuntu-24.04 F:/temp/WpSystem-my/Ubuntu-24.04/ext4.vhdx
wsl --import-in-place ubuntu_24.04docker F:\temp\WpSystem-my\Ubuntu-24.04\ext4.vhdx
wsl --manage ubuntu_24.04docker --set-sparse true
wsl --install Debian --name debian-13 --location F:/temp/WpSystem-my/debian
wsl --unregister  debian-13 # deleted also .vxdx  file
wsl -l -v
wsl --help
wsl --shutdown

**Podmain** on wsl (Debian) from intellij:
wsl --install Debian --name debian-1 --location F:/temp/WpSystem-my/debian-1
sudo apt update && sudo apt install -y git  \
 openssh-server \
 podman && \
sudo systemctl enable --now podman.socket && \
systemctl status podman.socket && \ 
systemctl --user enable --now podman.socket  && \
sudo apt install -y podman-docker # Or manually alias it: alias docker=podman
# Configure cgroup Manager if error 125 
mkdir ~/.config/containers
nano ~/.config/containers/containers.conf
[engine]
cgroup_manager = "cgroupfs"
events_logger = "file"

nano ~/.config/containers/registries.conf
unqualified-search-registries = ["docker.io"] # Podman does not assume docker.io is the default

wsl --shutdown # Restart your WSL
# ! Switch Debian to Legacy Iptables if Status 500 when run podmain
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
nano ~/.config/containers/containers.conf
[network]
firewall_driver = "iptables" 

wsl --shutdown # Restart your WSL
podman network rm podman
sudo systemctl restart podman.socket

SSL and nginx:
https://www.dynadot.com/ - registred , login , my info
https://www.dynadot.com/ru/domain/search and buy new DOMEN
https://www.dynadot.com/ru/account/domain/name/new_domains.html - 
  select row / Action / DNS setting
https://www.dynadot.com/ru/account/domain/name/list.html - 
open in Firewall TCP:443
gcloud compute ssh # SSH into your Debian instance
sudo apt update && sudo apt install certbot python3-certbot-nginx -y  # if nginx server
sudo nginx -t # path and test config
sudo systemctl reload nginx # nginx reload
sudo certbot --nginx -d boris-gra.xyz -d www.boris-gra.xyz # Obtain and Install SSL
  Enter an email address!!
  Agree to the Terms of Service.
  When prompted, choose whether to redirect HTTP traffic to HTTPS. Choosing option 2 (Redirect) is highly recommended
Your site should now be accessible via https://your_domain.com. Certbot also automatically sets up a timer or cron job for auto-renewal, ensuring your 90-day certificates are renewed before they expire.
https://search.google.com/search-console/welcome - registred domein in GCP
https://console.cloud.google.com/run/domains?project=vpn-gra  add domen for GCP Cloud Run
https://www.hostinger.com/uk/tutorials/how-to-set-up-nginx-reverse-proxy 

DELETE !!!
gsutil -m retention event release gs://boris-gra/images/*.*
gsutil retention temp release gs://boris-gra/images/*.*
</pre>