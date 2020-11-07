#!/bin/bash

# Configure the IP address
ip addr add 130.30.3.3/24 dev ens3
ip link set ens3 up

# Configure the DNS Server IP address
echo 'nameserver 130.30.3.254' > /etc/resolv.conf

# Repeatedly query www.bank.com
while true
do
    curl www.bank.com/query?username=Alice%password=4N4nD1nW0nD3rL4nD
    sleep 5
done