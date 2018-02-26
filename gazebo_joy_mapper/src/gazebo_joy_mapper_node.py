#!/usr/bin/env python
import rospy
import math
import numpy as np
from duckietown_msgs.msg import Twist2DStamped, BoolStamped
from sensor_msgs.msg import Joy, JointState
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Header
from __builtin__ import True

class GazeboJoyMapper(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))
        self.joy = None

        # Subscriptions
        self.sub_joy_ = rospy.Subscriber("joy", Joy, self.cbJoy, queue_size=1)

        # Publications
        self.pub_car_twist = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.pub_joint = rospy.Publisher('/joint_states', JointState, queue_size=10)

        #Setup Parameters
        self.v_gain = 1.0
        self.omega_gain = 1.0

    def cbJoy(self, joy_msg):
        self.joy = joy_msg
        self.publishControl()

    def publishControl(self):

        
        joint_cmd = JointState()
        joint_cmd.header = Header()
        joint_cmd.header.stamp = self.joy.header.stamp
        joint_cmd.name = ['left_wheel_joint', 'right_wheel_joint', 'aux_wheel_joint']
        joint_cmd.velocity = [self.joy.axes[1] * self.v_gain, 0.0, 0.0]
        joint_cmd.effort = [10, 10, 10]
        joint_cmd.position = [self.joy.axes[1] * self.v_gain, 0.0, 0.0]
        self.pub_joint.publish(joint_cmd)
        

        '''
        car_twist_msg = Twist()
        car_twist_msg.linear = Vector3(self.joy.axes[1] * self.v_gain, 0.0, 0.0) 
        car_twist_msg.angular = Vector3(0, 0, self.omega_gain * self.joy.axes[3])

        #rospy.loginfo("linear = %s \nangular = %s" %(self.joy.axes[1] , self.joy.axes[3]))
        #rospy.loginfo("linear = %s \nangular = %s" %(car_twist_msg.linear, car_twist_msg.angular))
        self.pub_car_twist.publish(car_twist_msg)
        '''


if __name__ == "__main__":
    rospy.init_node("gazebo_joy_mapper",anonymous=False)
    joy_mapper = GazeboJoyMapper()
    rospy.spin()
