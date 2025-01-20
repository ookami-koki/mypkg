#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

echo $ROS_DISTRO

colcon build
source $dir/.bashrc

ros2 run mypkg ipaddress & pub=$!

sleep 2

timeout 10 ros2 topic echo /ip_address > /tmp/mypkg.log

kill -9 $pub

cat /tmp/mypkg.log | 
grep -e 'hostname' -e 'address'

if  cat /tmp/mypkg.log | grep "'"  ||  cat /tmp/mypkg.log | grep "WARNING"  ; then
    exit 1
else
    exit 0
fi
