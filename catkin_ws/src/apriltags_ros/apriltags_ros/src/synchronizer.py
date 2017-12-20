import sensor_msgs
import message_filters
import rospy


rospy.init_node("apriltag_publisher")
caminfo_sub = message_filters.Subscriber("/raspicam_node/camera_info", sensor_msgs.CameraInfo)
image_sub = message_filters.Subscriber("/raspicam_node/image", sensor_msgs.Image)
apriltag1_pub = rospy.Publisher("/raspicam_node/camera_info", sensor_msgs.CameraInfo,  queue_size=1)
apriltag2_pub = rospy.Publisher("/raspicam_node/image", sensor_msgs.Image,  queue_size=1) 

def callback(j1, j2):
    #print j1, j2
    msg1 = sensor_msgs.CameraInfo( header = j1.header, 
                                     height = j1.height,
                                     width = j1.width,
                                     distortion_model = j1.distortion_model,
                                     D = j1.D,
                                     K = j1.K,
                                     R = j1.R,
                                     P = j1.P,
                                     binning_x = j1.binning_x,
                                     binning_y = j1.binning_y )

    msg2 = sensor_msgs.Image( header = j2.header, 
                                height = j2.height,
                                width = j2.width,
                                encoding = j2.encoding,
                                is_bigendian = j2.bigendian,
                                step = j2.step,
                                data = j2.data )

    apriltag1_pub.publish(msg1)
    apriltag2_pub.publish(msg2)
    
ts = message_filters.ApproximateTimeSynchronizer([caminfo_sub, image_sub], 20, 1)
ts.registerCallback(callback)

rospy.spin()
