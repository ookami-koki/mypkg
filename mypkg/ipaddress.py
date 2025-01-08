# SPDX-FileCopyrightText: 2024-2025 Koki Iwai
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socket

class Ipaddress(Node):
    def __init__(self):
        super().__init__("get_ipaddress_pub")
        self.pub = self.create_publisher(String, "ip_address", 10)
        self.create_timer(0.5, self.cb)

    def cb(self):
        check = self.get_ipaddress()
        if check:
            msg = String()
            msg.data = self.ip_address
            self.pub.publish(msg)

    def get_ipaddress(self):
        try:
            self.hostname = socket.gethostname()
            self.ip_address = socket.gethostbyname(self.hostname)
            return self.ip_address
        except Exception as e:
            print("Error")
            return None

def main():
    rclpy.init()
    node = Ipaddress()
    rclpy.spin(node)
