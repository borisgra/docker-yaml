#!/bin/bash

cd /home/boris/docker-yaml/yamls  # !!  boris  !!!
if [ ! -p myHostPipe ]; then
    sudo mkfifo myHostPipe &&  sudo chmod 777 myHostPipe 
fi
while true; do eval "$(cat myHostPipe)"; done
