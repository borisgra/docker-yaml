#!/bin/bash
#sudo systemctl stop hook.service
#sudo systemctl status hook.service


sudo chmod +x ./webhook_listener.sh && sudo chmod 777 ./webhook_listener.sh
sudo cp webhook_listener.sh /usr/bin && sudo cp hook.service /lib/systemd/system
sudo systemctl daemon-reload # reload this daemon each time after making any changes in .service file
sudo systemctl enable hook.service
sudo systemctl start hook.service