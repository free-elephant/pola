# Install before starting

#### UBUNTU 18.04 LTS 환경에서 로봇 운영체제(Robot Operating System)을 먼저 설치해야한다.
#### ROS는 UBUNTU 18.04 환경에서 melodic으로 설치해야한다. 
#### ROS는 설치하면 python 2.7 에서 작동하기 때문에, python 3.x 버젼에서 사용할 수 있게 환경설정을 해주어야 한다.
### 이 글에서 방법을 소개하고자 한다.
***
# _How to setup ROS with Python 3_
## 1. Install ROS Melodic
### 1.1 source.list 설정
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $ (lsb_release -sc) main"> /etc/apt/sources.list.d/ros-latest.list'
```
### 1.2 키 설정
```
$ sudo apt-key adv --keyserver 'hkp : //keyserver.ubuntu.com : 80'--recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```
### 1.3 NTP(Network Time Protocol) 설정
```
$ sudo apt-get install -y chrony ntpdate
$ sudo ntpdate -q ntp.ubuntu.com
```
### 1.4 패키지 업데이트
```
$ sudo apt-get update && sudo apt-get upgrade -y
```
### 1.5 ROS Melodic 설치
```
$ sudo apt install ros-melodic-desktop-full
$ sudo apt-get install ros-kinetic-rqt*
```
### 1.6 rosdep 초기화
```
$ sudo rosdep init
$ rosdep update
```
### 1.7 환경 설정
```
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```
### 1.8 rosinstall 설치
```
$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```
## 2. Install realsense-sdk 2.0
```
pola README.md에 realsense-sdk 설치 방법을 적어놓았다. 만약 설치하지 않았다면
https://github.com/IntelRealSense/realsense-ros 로 가서 설치하기 바람.
```
### 2.1 realsense catkin make
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
$ cd ..
$ catkin_make
```
### 2.1 realsense library install python
```
$ pip install realsense2
```
***
### ** 해당지점까지 완료하면 ROS는 python 2.7에서 작동하게 된다.
***
## 3. Erase python 2.7 and reinstall ROS
### 3.1 Erase python 2.7
```
$ sudo apt purge python2.7-minimal   
$ sudo apt-get install python3-dev 
```
### 3.2 Install ROS melodic
```
# 위에 1번 과정을 반복하면 된다.
```
### 3.3 Install Realsense sdk 2.0
```
# 위에 2번 과정을 반복하면 된다.
$ realsense-viewer # 실행되면 성공
```
### ** ROS를 재설치할 때 python 2.7이 다시 설치된다.
***
### 3.4 필요한 패키지 git clone
```
$ cd catkin_ws/src
$ git clone https://github.com/ros/geometry
$ git clone https://github.com/ros/geometry2
$ (* turtlebot3)  git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
```
### 3.5 가상환경에서 필요한 라이브러리 설치
```
pip install catkin_pkg pyyaml empy rospkg numpy
```
### 3.6 catkin_make
```
catkin_make
source devel/setup.bash
sudo apt-get install ros-melodic-ddynamic-reconfigure
```
### 3.7 sys.path 확인
```
$ workon cv4
$ python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
```
# Result
![mapping](https://user-images.githubusercontent.com/46383014/73356963-da3fab00-42de-11ea-8a6d-06a07113587a.png)
### python 2.7이 path 추가 되었으면 성공함.
