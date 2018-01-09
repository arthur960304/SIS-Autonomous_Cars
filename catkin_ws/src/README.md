How to run RPi Camera
========================================================================================
  1) If you want to run the normal resolution, run the code below
    
    roslaunch raspicam_node camerav2_1280x960.launch
    
  2) If you want to run in lower resolution and lower frame rate, run teh code below
    
    roslaunch raspicam_node camerav2_revised.launch
    
  3) Transform the image info type
  
    rosrun image_transport republish compressed in:=/raspicam_node/image raw out:=/raspicam_node/image
    
  4) In order to publish two topics (/raspicam_node/camera_info and /raspicam_node/image) at the same time
  
    rosrun apriltags_ros camInfo_publisher.py
    
How to run Apriltag Detector
========================================================================================
    roslaunch apriltags_ros example.launch
