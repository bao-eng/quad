#!/usr/bin/python

import rospy

from sensor_msgs.msg import Joy
from sensor_msgs.msg import JointState
from ackermann_msgs.msg import AckermannDrive
from std_msgs.msg import Float32

def maprange( a, b, s):
    (a1, a2), (b1, b2) = a, b
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.axes[0])
    
    steer_msg = JointState()
    steer_msg.position = []
    steer_msg.name = []
    steer_msg.position.append(data.axes[0])#maprange( (-1, 1), (-100, 100), data.axes[0])
    steer_msg.position.append(data.axes[0])
    steer_msg.name.append('FL_upright_joint')
    steer_msg.name.append('FR_upright_joint')
    steer_publisher.publish(steer_msg)
    #rospy.Publisher()
    #pub.publish([data.axes[0],0,0,0,0])
if __name__ == '__main__':
    rospy.init_node("quad_teleop", anonymous=False)
    rospy.Subscriber("joy", Joy, callback)
    steer_publisher = rospy.Publisher('steering', JointState, queue_size=1)
    while not rospy.is_shutdown():
        rospy.spin() 
   
