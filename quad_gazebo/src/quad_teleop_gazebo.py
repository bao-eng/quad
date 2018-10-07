#!/usr/bin/python

import rospy
import math
from ackermann_msgs.msg import AckermannDrive
from ackermann_msgs.msg import AckermannDriveStamped
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32

def maprange( a, b, s):
    (a1, a2), (b1, b2) = a, b
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.axes[0])

    ack_cmd = AckermannDriveStamped()
    ack_cmd.header.stamp = rospy.Time.now()
    drive = AckermannDrive()
    drive.speed = (data.axes[5])
    drive.steering_angle = (data.axes[0])
    ack_cmd.drive = drive
    ack_publisher.publish(ack_cmd)
    #rospy.Publisher()
    #pub.publish([data.axes[0],0,0,0,0])
if __name__ == '__main__':
    rospy.init_node("quad_teleop", anonymous=False)
    rospy.Subscriber("joy", Joy, callback)
    ack_publisher = rospy.Publisher('ack_steer', AckermannDriveStamped, queue_size=10)
    while not rospy.is_shutdown():
        rospy.spin() 
   
