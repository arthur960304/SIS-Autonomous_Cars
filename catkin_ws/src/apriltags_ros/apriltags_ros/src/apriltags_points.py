#!/usr/bin/env python
import roslib
import rospy
import tf
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker

def show_points(trans, frame):
    rate = rospy.Rate(5)
    triplePoints = []
    #transform from x,y points to x,y,z points
    p = Point() 
    p.x = trans[0]
    p.y = trans[1]
    p.z = trans[2]
    triplePoints.append(p)

    iterations = 0
    while not rospy.is_shutdown() and iterations <= 1:
        pub = rospy.Publisher(frame, Marker, queue_size = 100)
        marker = Marker()
        marker.header.frame_id = "/map"

        marker.type = marker.POINTS
        marker.action = marker.ADD
        marker.pose.orientation.w = 1

        marker.points = triplePoints
        t = rospy.Duration()
        marker.lifetime = t
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0

        pub.publish(marker)
        iterations += 1
        rate.sleep()
	
if __name__ == "__main__" :
	rospy.init_node("apriltags_points")

	ls = tf.TransformListener()
	trans = [0] * 3
	origin_trans = trans
	time = 1
	while not rospy.is_shutdown():
		try:
			(trans1,rot1) = ls.lookupTransform('/map', '/base_link', rospy.Time(0))
			(trans2,rot1) = ls.lookupTransform('/base_link', '/raspicam', rospy.Time(0))
			(trans3,rot2) = ls.lookupTransform('/raspicam', '/tag_21', rospy.Time(0))
			x = trans3[0]
			y = trans3[1]
			z = trans3[2]
			trans3[0] = z
			trans3[1] = -x
			trans3[2] = -y
			if (time <= 10) : 
				trans[0] = trans1[0] + trans2[0] + trans3[0]
				trans[1] = trans1[1] + trans2[1] + trans3[1]
				trans[2] = trans1[2] + trans2[2] + trans3[2]
				time += 1
				origin_trans = trans
<<<<<<< HEAD
				show_points(trans, "tag_21")
			else : 
=======
				show_points(trans, "tag21")
			else :
>>>>>>> c7787f3f1a847ffe929a28f1f33930cb08f52f84
				show_points(origin_trans, "tag_21")
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue
