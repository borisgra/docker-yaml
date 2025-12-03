#!/bin/bash
# create and start computer instance GCP
#gcloud auth login
"""
curl -s https://raw.githubusercontent.com/borisgra/docker-yaml/develop/win10gcp.sh | \
  bash -s -- -n win10gcp -d pd-balanced
"""

usage() {
    echo "Usage: $0 -n <name> -t <tipe instance> -d <disk_type> -p <project> -z <zone> -l <location>"
    exit 1
}

# Initialize variables
name="win10-user-123456"
project="com-gra"
zone="us-central1-a"
location="us-central1"
type="e2-standard-2"
disk_type="pd-standard" # pd-standard=1$ / pd-balanced=2.5$ / pd-ssd=4.25$

# Parse command line options
while getopts "n:p:z:t:d:l" opt; do
    case $opt in
        n)
            name=$OPTARG
            ;;
        p)
            project=$OPTARG
            ;;
        z)
            zone=$OPTARG
            ;;
        l)
            location=$OPTARG
            ;;
        t)
            type=$OPTARG
            ;;
        d)
            disk_type=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            usage
            ;;
        :)
            echo "Option -$OPTARG requires an argument."
            usage
            ;;
    esac
done

date
echo "$name $type $disk_type $project $zone $location"
echo "    DOWNLOADING WINDOWS IMAGE FILE... ~5min"

# images - 6min  5.9G
gcloud compute images create $name \
--source-uri=gs://public-gra/images/image-gcp-win10-user-123456.tar.gz \
--project=$project \
--storage-location=$location

date
echo "IMAGE created"

# disk type (25gb): pd-standard=1$ / pd-balanced=2.5$ / pd-ssd=4.25$
#  1 min
gcloud compute instances create $name \
--project=$project \
--zone=$zone \
--machine-type=$type \
--network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
--maintenance-policy=MIGRATE \
--provisioning-model=STANDARD \
--create-disk=auto-delete=yes,boot=yes,device-name=$name,image=projects/com-gra/global/images/$name,mode=rw,\
size=25,type=$disk_type

date
echo "delete win10 image"
gcloud compute images delete $name \
--project=$project

echo "All done"
