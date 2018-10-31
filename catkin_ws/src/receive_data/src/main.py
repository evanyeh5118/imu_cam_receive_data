#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from receive_data import setupSocket, revceiveImuData

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
	message = revceiveImuData()
	print message
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
	setupSocket()
        talker()
    except rospy.ROSInterruptException:
        pass
