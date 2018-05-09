#!/usr/bin/env python

#imports files needed to run
import string
import urllib2
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def Flight():
    #start node
    rospy.init_node('bebop_plan', anonymous=True)
    velocity_publisher = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
    #takeoff_publisher = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
    #land_publisher = rospy.Publisher('/bebop/land', Empty, queue_size=10)
    vel_msg = Twist()
    #take_msg = Empty()

    #takeoff and land
    #take_msg

    duration = 2
    DeltT= 0
    # current time
    t0 = rospy.Time.now().to_sec()

    #velocity of drone
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 1
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Loop to go for specified time
        while (DeltT < duration):
            DeltT = (rospy.Time.now().to_sec() - t0)
            #takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            print (DeltT)
        #After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg.linear.x)
        #land_publisher.publish('once')

if __name__ == '__main__':
    try:
        Flight()
    except rospy.ROSInterruptException: pass
