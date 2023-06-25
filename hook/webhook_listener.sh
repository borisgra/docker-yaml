#!/bin/bash
# sudo chmod +x ./webhook_listener.sh

# sudo cp webhook_listener.sh /usr/bin && sudo cp hook.service /lib/systemd/system

if [ ! -f 'myHostPipe' ]; then
    sudo mkfifo myHostPipe &&  sudo chmod 777 myHostPipe 
fi
while true; do eval "$(cat myHostPipe)"; done
