from roscr_bridge_interfaces.srv import IsimpleLedControl

import rclpy
from rclpy.node import Node
# from time import sleep
import time
import serial




def openSerial(port="/dev/ttyACM0", speed = 115200):
    try:
        s = serial.Serial(port, speed) 
            
    except serial.SerialException as e:
        if e.errno == 13:
            raise e
        pass
    except OSError:
        pass
    return s


# ser = serial.Serial ("/dev/ttyACM0", 115200) #Open port with baud rateif __name__ == '__main__':
# ser.write(0x31) #transmit data serially
# time.sleep(2)
# ser.write(0x32) #transmit data serially
# time.sleep(2)
# ser.write(0x33) #transmit data serially
# time.sleep(2)
# ser.write(0x34) #transmit data serially
# time.sleep(2)

ser = openSerial()

class LedControlServer(Node):

    def __init__(self):
        super().__init__('led_control_server')
        self.srv = self.create_service(IsimpleLedControl, 'led_control', self.service_callback)

    def service_callback(self, request, response):
        if request.command == 1:
            response.is_success = True
        else:
            response.is_success = False 
        self.get_logger().info('Command: %d' % request.command)
        # 여기 이부분에 OpenCR과 시리얼 통신을 하는 코드가 들어가게 됩니다.

        key = request.command
        if key == 1:
            self.get_logger().info("key == '1'")
            #코드 시작
            # ser.write(0x31) #transmit data serially
            ser.write(bytes('1','utf-8'))
            # time.sleep(2)
            #코드 끝
            '''
            '''
        elif key == 2:
            self.get_logger().info("key == '2'")
            #코드 시작
            # ser.write(0x32) #transmit data serially
            ser.write(bytes('2','utf-8'))
            # time.sleep(2)
            #코드 끝
        elif key == 3:
            self.get_logger().info("key == '3'")
            #코드 시작
            # ser.write(0x33) #transmit data serially
            ser.write(bytes('3','utf-8'))
            # time.sleep(2)
            #코드 끝
        elif key == 4:
            self.get_logger().info("key == '4'")
            #코드 시작
            # ser.write(0x34) #transmit data serially
            ser.write(bytes('4','utf-8'))
            # time.sleep(2)
            #코드 끝
        if key == 5:
            self.get_logger().info("key == '5'")
            #코드 시작
            # ser.write(0x31) #transmit data serially
            ser.write(bytes('5','utf-8'))
            # time.sleep(2)
            #코드 끝
            '''
            '''
        elif key == 6:
            self.get_logger().info("key == '6'")
            #코드 시작
            # ser.write(0x32) #transmit data serially
            ser.write(bytes('6','utf-8'))
            # time.sleep(2)
            #코드 끝
        elif key == 7:
            self.get_logger().info("key == '7'")
            #코드 시작
            # ser.write(0x33) #transmit data serially
            ser.write(bytes('7','utf-8'))
            # time.sleep(2)
            #코드 끝
        elif key == 8:
            self.get_logger().info("key == '8'")
            #코드 시작
            # ser.write(0x34) #transmit data serially
            ser.write(bytes('8','utf-8'))
            # time.sleep(2)
            #코드 끝
        elif key == 9:
            self.get_logger().info("key == '9'")
            #코드 시작
            # ser.write(0x34) #transmit data serially
            ser.write(bytes('9','utf-8'))
            # time.sleep(2)
            #코드 끝


        return response


def main(args=None):
    rclpy.init(args=args)

    led_control_server = LedControlServer()

    rclpy.spin(led_control_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()