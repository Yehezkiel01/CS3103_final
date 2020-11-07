#!/bin/bash
cp ip.service /lib/systemd/system/dns.service
cp ip.sh /home/user/Documents/ip.sh

sudo systemctl daemon-reload

sudo systemctl enable ip.service

sudo systemctl start ip.service