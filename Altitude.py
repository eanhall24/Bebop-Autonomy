#!/usr/bin/env python

#imports files needed to run
import string
import urllib2
import rospy
import time
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
from bebop_msgs.msg import Ardrone3PilotingStatePositionChanged
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def Altitude():
    #start node
    rospy.init_node('bebop_plan', anonymous=True)
    velocity_publisher = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
    #altitude_publisher = rospy.Publisher('/bebop/states/ardrone3/PilotingState/AltitudeChanged', Ardrone3PilotingStateAltitudeChanged, queue_size=10)
    #takeoff_publisher = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
    #land_publisher = rospy.Publisher('/bebop/land', Empty, queue_size=10)
    vel_msg = Twist()
    #alt_msg = Ardrone3PilotingStateAltitudeChanged()
    alt_msg = Ardrone3PilotingStatePositionChanged()
    #take_msg = Empty()


    #Target Altitude
    Goal = 1
    Current = alt_msg.altitude

    #velocity of drone
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = -1
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Rising Loop
        while (Current < Goal):
            Current = alt_msg.altitude
            #takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            print (Current)
        #After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        #print (vel_msg.linear.z)
        #land_publisher.publish('once')

        #Descend Loop
        #while (Current > Goal):
            #velocity_publisher.publish(vel_msg)
        #After the loop stops
        #vel_msg.linear.x = 0
        #vel_msg.linear.y = 0
        #vel_msg.linear.z = -1
        #vel_msg.angular.x = 0
        #vel_msg.angular.y = 0
        #vel_msg.angular.z = 0
        #velocity_publisher.publish(vel_msg)
        #print (vel_msg.linear.z)

        #Hover Loop
        #while (Current == Goal):
            #velocity_publisher.publish(vel_msg)
        #After the loop stops
        #vel_msg.linear.x = 0
        #vel_msg.linear.y = 0
        #vel_msg.linear.z = 0
        #vel_msg.angular.x = 0
        #vel_msg.angular.y = 0
        #vel_msg.angular.z = 0
        #velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        Altitude()
    except rospy.ROSInterruptException: pass
