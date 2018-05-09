#!/usr/bin/env python

#imports files needed to run
import string
import urllib2
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def Square():
    #start node
    rospy.init_node('bebop_plan', anonymous=True)
    velocity_publisher = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
    #takeoff_publisher = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
    #land_publisher = rospy.Publisher('/bebop/land', Empty, queue_size=10)
    vel_msg = Twist()
    #take_msg = Empty()

    #takeoff and land
    #take_msg

    duration = 32
    DeltT= 0
    # current time
    t0 = rospy.Time.now().to_sec()

    #velocity of drone
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Loop for first line
        while (DeltT < 4):
            DeltT = (rospy.Time.now().to_sec() - t0)
            #start moving (m/s)
            vel_msg.linear.x = 0.05
            print (vel_msg)
            #takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
        #After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        #Loop for first turn
        while (4 < DeltT < 8):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.angular.z = 0.1
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for second line
        while (8 < DeltT < 12):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.linear.x = 0.05
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for second turn
        while (12 < DeltT < 16):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.angular.z = 0.1
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for third line
        while (16 < DeltT < 20):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.linear.x = 0.05
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for third turn
        while (20 < DeltT < 24):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.angular.z = 0.1
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for fourth line
        while (24 < DeltT < 28):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.linear.x = 0.05
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)

        # Loop for third turn
        while (28 < DeltT < duration):
            DeltT = (rospy.Time.now().to_sec() - t0)
            # start moving (m/s)
            vel_msg.angular.z = 0.1
            print (vel_msg)
            # takeoff_publisher.publish(once)
            velocity_publisher.publish(vel_msg)
            # After the loop stops
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        print (vel_msg)
        #land_publisher.publish('once')

if __name__ == '__main__':
    try:
        Square()
    except rospy.ROSInterruptException: pass
