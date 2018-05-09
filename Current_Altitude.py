#!/usr/bin/env python


import string
import urllib2
import rospy
import time
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
from bebop_msgs.msg import Ardrone3PilotingStatePositionChanged
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


def callback(data):
    rospy.loginfo(data.data)

def Current_Altitude():
    rospy.init_node('bebop_altitude', anonymous=True)
    rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AltitudeChanged', Ardrone3PilotingStateAltitudeChanged, callback)

    alt_msg = Ardrone3PilotingStateAltitudeChanged()
    print(alt_msg)

    rospy.spin()
    
if __name__ == '__main__':
    try:
        Current_Altitude()
    except rospy.ROSInterruptException: pass
