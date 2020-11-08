#!/bin/bash

# Configure the IP address
ip addr add 130.30.3.254/24 dev ens3
ip link set ens3 up