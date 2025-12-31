import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

class CpuPublisher(Node):
    def __init__(self):
        super().__init__('cpu_publisher')
        self.pub = self.create_publisher(Float32, 'cpu_usage', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = psutil.cpu_percent()
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}%')

def main():
    rclpy.init()
    node = CpuPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
