# SPDX-FileCopyrightText: 2024-2025 Koki Iwai
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socket

rclpy.init()
node = Node("ip_address_pub")
pub= node.create_publisher(String, "ip_address", 10)

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print("Error")
        return None

def cb():
    ip_address = get_ip_address()
    if ip_address:
        msg = String()
        msg.data = ip_address
        pub.publish(msg)
        node.get_logger().info(f'{ip_address}')
    else:
        node.get_logger().warn('Failed')

def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
