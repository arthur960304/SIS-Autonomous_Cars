# SIS-Autonomous_Cars
## Hardware Architecture
### Equipment
- Raspberry Pi 3 Model B
- RPLidar A1
- Arduino UNO
- Arduino Car Chassis Kit
- L298N Motor Drive Board
- Lipo Battery
- Mobile Power

## Software Setup
### Environment setting
- [Ubuntu mate 16.04](https://ubuntu-mate.org/download/)
- [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)
- [Install the Arduino Software (IDE) on on Linux](https://www.arduino.cc/en/Guide/Linux)
- Control Arduino through ROS
    - [rosserial_arduino](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)
    - [Arduino and Ros](https://hackmd.io/s/rkCGJ0vfZ)
- [RPLidar SKD](https://www.slamtec.com/en/Support#rplidar-a1)
    - [rplidar-ROS Wiki](http://wiki.ros.org/rplidar)

#### RPLidar
##### Test1
- 在rpi上跑RPlidar並在電腦上使用rviz看到資料
:::warning
1. 每次`catkin_make`之後要記得`source /devel/setup.bash`做路徑與環境的設定
2. 不能用電腦的usb給rpi供電，因為電流會不夠，會沒辦法看到rplidar的資料
:::
- step1: 設定rosmaster
    - remote pc
        - ROS_MASTER_URI = `remote_pc_ip`
        - ROS_HOSTNAME = `remote_pc_ip`
    - rpi
        - ROS_MASTER_URI = `remote_pc_ip`
        - ROS_HOSTNAME = `rpi_ip`
- step2: 在電腦端執行roscore
- step3: rpi上執行`roslaunch rplidar_ros rplidar.launch`
其中，`RPLidar helth status:0`是正常的
![](https://i.imgur.com/e7jbJiq.png)
- step4: 在rpi即remote pc兩邊都看`rostopic list`是否有`/scan`
    - remote pc
    ![](https://i.imgur.com/VH4LwDZ.png)
    - rpi
    ![](https://i.imgur.com/BdXsPg1.png)
- 在remote pc上執行`rostopic echo /scan`看電腦端是否有收到rplidar所發送的資訊
- 確定有收到資訊後，在remote pc端執行`rviz`
![](https://i.imgur.com/0NlRILl.png)
- `rqt_graph`
執行`rosrun rplidar_ros rplidarNodeClient`可以看到執行結果
![](https://i.imgur.com/ypvkbtP.png)
 ![](https://i.imgur.com/cyzjsPp.png)

##### Test2
- 測試`hector-slam`
- step1: 安裝hector slam`sudo apt-get install ros-kinetic-hector-slam`
- step2: 在rpi上執行 (每一個都要開一個新的terminal)
```=
roslaunch rplidar_ros rplidar.launch
roslaunch rplidar_ros hectormapping.launch
```
- 在兩邊都執行`rostopic list`確認是否有更新資料
    - remote pc
    ![](https://i.imgur.com/Ws2jHyk.png)
    - rpi
![](https://i.imgur.com/2Lwkxg1.png)

- step3: 執行`rosrun rplidar_ros rplidarNodeClient`確保兩邊資料有連結
    - Node only![](https://i.imgur.com/ZyZCh1h.png)
    - Node/Topic (active)![](https://i.imgur.com/ywq2Y74.png)
    - Node/Topic (all)![](https://i.imgur.com/By1qaqf.png)
- step4: 執行rviz看結果
![](https://i.imgur.com/fGcZDW1.png)

:::warning
[待解決]目前遇到的問題：
![](https://i.imgur.com/rGvYGWA.png)

:::
