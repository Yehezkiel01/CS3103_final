#!/bin/bash
cp -r ../app /home/user/Documents/app
cp ip.sh /home/user/Documents/ip.sh

cp ip.service /lib/systemd/system/ip.service
cp dns.service /lib/systemd/system/dns.service
cp flask.service /lib/systemd/system/flask.service

sudo systemctl daemon-reload

sudo systemctl enable dns.service
sudo systemctl enable flask.service
sudo systemctl enable ip.service

sudo systemctl start dns.service
sudo systemctl start flask.service
sudo systemctl start ip.service