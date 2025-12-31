import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class LoadAlert(Node):
    def __init__(self):
        super().__init__('load_alert')
        self.declare_parameter('threshold', 50.0)
        self.sub = self.create_subscription(Float32, 'cpu_usage', self.callback, 10)

    def callback(self, msg):
        th = self.get_parameter('threshold').value
        if msg.data > th:
            self.get_logger().warn(f'ALERT: High Load {msg.data}% (Threshold: {th}%)')
        else:
            self.get_logger().info(f'Normal: {msg.data}%')

def main():
    rclpy.init()
    node = LoadAlert()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
