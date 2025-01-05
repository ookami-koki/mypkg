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
            self.get_logger().info(f'{self.ip_address}')
        else:
            self.get_logger().warn('Failed')



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
