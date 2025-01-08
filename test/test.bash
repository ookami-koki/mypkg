#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ros2 run mypkg ipaddress & pub=$!

timeout 10 ros2 topic echo /ip_address > /tmp/mypkg.log

kill -9 $pub

if cat /tmp/mypkg.log | grep "'" ; then
    exit 1
else
    exit 0
fi


