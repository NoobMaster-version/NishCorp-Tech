#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from tf_transformations import euler_from_quaternion

class ImuSubscriber(Node):
    def __init__(self):
        super().__init__('imu_subscriber')
        self.subscription = self.create_subscription(
            Imu,
            '/imu',
            self.imu_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('IMU Subscriber Node has been started.')

    def imu_callback(self, msg):
        orientation_q = msg.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

        self.get_logger().info(f'Roll: {roll:.2f} radians ({roll * 180 / 3.14159:.2f} degrees), '
                               f'Pitch: {pitch:.2f} radians ({pitch * 180 / 3.14159:.2f} degrees)')

def main(args=None):
    rclpy.init(args=args)
    imu_subscriber = ImuSubscriber()
    rclpy.spin(imu_subscriber)
    imu_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
