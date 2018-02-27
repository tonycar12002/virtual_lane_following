#!/usr/bin/env python
import rospy
import math
import numpy as np
from duckietown_msgs.msg import Twist2DStamped, BoolStamped
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Header
import time
from __builtin__ import True

class GazeboJoyMapper(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))
        self.joy = None
        self.linear = 0
        self.angular = 0 

        # Subscriptions
        self.sub_joy_ = rospy.Subscriber("joy", Joy, self.cbJoy, queue_size=1)

        # Publications
        self.pub_car_twist = rospy.Publisher("/duckiebot_velocity_controller/cmd_vel", Twist, queue_size=1)

        #Setup Parameters
        self.v_gain = 1.0
        self.omega_gain = 1.0

        rospy.Timer(rospy.Duration(0.2), self.send_carcmd)

    def cbJoy(self, joy_msg):
        self.joy = joy_msg
        self.publishControl()

    def publishControl(self):

        self.linear = self.joy.axes[1] * self.v_gain
        self.angular = self.omega_gain * self.joy.axes[3]
         
    def send_carcmd(self, event):

        car_twist_msg = Twist()
        car_twist_msg.linear = Vector3(self.linear, 0.0, 0.0) 
        car_twist_msg.angular = Vector3(0, 0, self.angular)
        self.pub_car_twist.publish(car_twist_msg)

if __name__ == "__main__":
    rospy.init_node("gazebo_joy_mapper",anonymous=False)
    joy_mapper = GazeboJoyMapper()
    rospy.spin()
