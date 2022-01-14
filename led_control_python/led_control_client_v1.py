import sys

from roscr_bridge_interfaces.srv import IsimpleLedControl
import rclpy
from rclpy.node import Node


class LedControlClient(Node):

    def __init__(self):
        super().__init__('led_control_client')
        self.client = self.create_client(IsimpleLedControl, 'led_control') # Client builder 패턴
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service server...')
        self.req = IsimpleLedControl.Request()

    def send_request(self):
        # self.req.command = int(input())
        self.req.command = int(self.main_menu())
        self.future = self.client.call_async(self.req)

    def main_menu(self):
        print("-------------------------------------------------")
        print(" LIST MENU")
        print("-------------------------------------------------")
        print('1. led 1번)')
        print('2. led 2번)')
        print('3. led 3번)')
        print('4. led 4번)')
        print('5. led ALL OFF)')
        print('6. led ALL ON)')
        print('7. led Sequencial 1->4)')
        print('8. led Sequencial 4->1)')
        print('9. wheel motor rotation)')
        
        # print("-------------------------------------------------")
        # print(" q.  QUIT")
        # print("-------------------------------------------------")
        # print()
        #print("SELECT THE COMMAND NUMBER : ")
        key = input("SELECT THE COMMAND NUMBER : ")
        return key


def main(args=None):
    rclpy.init(args=args)

    led_control_client = LedControlClient()
 
    while(1):
        led_control_client.send_request()
        while rclpy.ok():
            rclpy.spin_once(led_control_client)
            if led_control_client.future.done():
                try:
                    response = led_control_client.future.result()
                except Exception as e:
                    led_control_client.get_logger().info(
                        'Service call failed: %r' % (e,))
                else:
                    if response.is_success:
                        led_control_client.get_logger().info("success")
                    else:
                        led_control_client.get_logger().info("false")
                break

    led_control_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()