#!/usr/bin/env python
import apriltags_ros.msg
import sensor_msgs.msg
import message_filters
import rospy

rospy.init_node("camInfo_publisher")
caminfo_sub = message_filters.Subscriber("/raspicam_node/camera_info", sensor_msgs.msg.CameraInfo)
image_sub = message_filters.Subscriber("/raspicam_node/image", sensor_msgs.msg.Image)
apriltag1_pub = rospy.Publisher("/camera/image_raw/camera_info", sensor_msgs.msg.CameraInfo,  queue_size=10)
apriltag2_pub = rospy.Publisher("/camera/image_raw/image", sensor_msgs.msg.Image,  queue_size=10) 

def callback(j1, j2):
    #print j1, j2
    msg1 = sensor_msgs.msg.CameraInfo( header = j1.header, 
                                     height = j1.height,
                                     width = j1.width,
                                     distortion_model = j1.distortion_model,
                                     D = j1.D,
                                     K = j1.K,
                                     R = j1.R,
                                     P = j1.P,
                                     binning_x = j1.binning_x,
                                     binning_y = j1.binning_y )

    msg2 = sensor_msgs.msg.Image( header = j2.header, 
                                height = j2.height,
                                width = j2.width,
                                encoding = j2.encoding,
                                is_bigendian = j2.is_bigendian,
                                step = j2.step,
                                data = j2.data 	)

    apriltag1_pub.publish(msg1)
    apriltag2_pub.publish(msg2)
    
ts = message_filters.ApproximateTimeSynchronizer([caminfo_sub, image_sub], 20, 1)
ts.registerCallback(callback)

rospy.spin()
