#!/usr/bin/env python

import rospy

from publish_utils import *


	
'''
def listener():
	
	rospy.init_node('database',anonymous = True)
	rospy.Subscriber("/pre_obstacle", String, server.pre)
	rospy.Subscriber('/pubmoos/WAMV_X', Float64,server.wamv_x_callback)
	rospy.Subscriber('/pubmoos/WAMV_Y', Float64,server.wamv_y_callback)
	rospy.Subscriber('/pubmoos/WAMV_YAW', Float64,server.wamv_yaw_callback)

	wamv_x_sub = message_filters.Subscriber('/pubmoos/WAMV_X', Float64)

	wamv_y_sub = message_filters.Subscriber('/pubmoos/WAMV_Y', Float64)

	wamv_yaw_sub = message_filters.Subscriber('/pubmoos/WAMV_YAW', Float64)

	#preobstacle_sub = message_filters.Subscriber('/pre_obstacle', String)

	ts = message_filters.ApproximateTimeSynchronizer([wamv_x_sub, wamv_y_sub,wamv_yaw_sub], 10, 1, allow_headerless=True)

	ts.registerCallback(callback)
	
	#rate = rospy.Rate(1)
	
	
	rospy.spin()

'''
if __name__ == '__main__':
	rospy.init_node('database',anonymous = True)
	server = Server()

	print('hello??')
	rospy.init_node('database',anonymous = True)
	rospy.Subscriber('/pre_obstacle', String, server.pre_callback)
	rospy.Subscriber('/pubmoos/WAMV_X', Float64,server.wamv_x_callback)
	rospy.Subscriber('/pubmoos/WAMV_Y', Float64,server.wamv_y_callback)
	rospy.Subscriber('/pubmoos/WAMV_YAW', Float64,server.wamv_yaw_callback)
	rospy.spin()
