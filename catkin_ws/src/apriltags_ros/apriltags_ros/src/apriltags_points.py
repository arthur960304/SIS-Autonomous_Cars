#!/usr/bin/env python
import roslib
import rospy
import tf
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker

if __name__ == "__main__" :
	rospy.init_node("apriltags_points")

	ls = tf.TransformListener()

	while not rospy.is_shutdown():
		try:
			(trans1,rot1) = ls.lookupTransform('/map', '/base_link', rospy.Time(0))
			(trans2,rot1) = ls.lookupTransform('/base_link', '/raspicam', rospy.Time(0))
			(trans3,rot2) = ls.lookupTransform('/raspicam', '/tag_21', rospy.Time(0))
			trans.x = trans1.x + trans2.x + trans3.x
			trans.y = trans1.y + trans2.y + trans3.y
			trans.z = trans1.z + trans2.z + trans3.z
			show_points(self, trans, /tag21)
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue

def show_points(self, trans, frame):
    rate = rospy.Rate(5)
    triplePoints = []
     #transform from x,y points to x,y,z points
        p = Point() 
        p.x = trans.x
        p.y = trans.y
        p.z = trans.z
        triplePoints.append(p)

    iterations = 0
    while not rospy.is_shutdown() and iterations <= 10:
        pub = rospy.Publisher(frame, Marker, queue_size = 100)
        marker = Marker()
        marker.header.frame_id = "/map"

        marker.type = marker.POINTS
        marker.action = marker.ADD
        marker.pose.orientation.w = 1

        marker.points = triplePoints
        t = rospy.Duration()
        marker.lifetime = t
        marker.scale.x = 0.4
        marker.scale.y = 0.4
        marker.scale.z = 0.4
        marker.color.a = 1.0
        marker.color.r = 1.0

        pub.publish(marker)
        iterations += 1
        rate.sleep()