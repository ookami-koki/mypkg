#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ros2 run mypkg ipaddress & pub=$!

timeout 10 ros2 topic echo /ip_address > /tmp/mypkg.log

kill -9 $pub

cat /tmp/mypkg.log | 
grep -e 'hostname' -e 'address'

cat /tmp/mypkg.log |
grep "\'" && exit 1
