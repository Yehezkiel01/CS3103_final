#!/bin/bash
cp -r ../app /home/users/Documents/app

cp dns.service /lib/systemd/system/dns.service
cp flask.service /lib/systemd/system/flask.service

sudo systemctl daemon-reload

sudo systemctl enable dns.service
sudo systemctl enable flask.service

sudo systemctl start dns.service
sudo systemctl start flask.service