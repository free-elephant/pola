# Introduction
#### Hector Slam 을 하기 위해서는 Google에서 제공하는 Cartographer ROS를 설치해야 한다.
#### Cartographer 는 여러 플랫폼 및 센서 구성에서 2D 및 3D 로 SLAM(Simultaneous localization and mapping)을 제공하는 시스템이다.
#### UBUNTU 18.04 에서는 ROS melodic을 지원하므로 melodic 환경에서 ubuntu를 설치한다.
***
## Install Cartographer ROS
### Building & Installation
```
$ sudo apt-get update
$ sudo apt-get install -y python-wstool python-rosdep ninja-build
```
### Create Workspace
```
$ mkdir carto_ws
$ cd carto_ws
$ wstool init src
$ wstool merge -t src https://raw.githubusercontent.com/googlecartographer/cartographer_ros/master/cartographer_ros.rosinstall
$ wstool update -t src
```
### Install Cartographer_ros Dependencies
```
$ src/cartographer/scripts/install_proto3.sh
$ sudo rosdep init
$ rosdep update
$ rosdep install --from-paths src --ignore-src --rosdistro=melodic -y
```
### Build & Install 
```
$ catkin_make_isolated --install --use-ninja
```
***
## YDLIDAR G2 - Hector Slam Example
#### 설치한 Google Cartographer 를 이용해서 Hector Slam 을 구현해본다. 

#### 1. git clone해서 src directory로 복사
```
$ git clone https://github.com/kieunbi/pola.git
```
#### 2. ydlidar_ws directory 에 있는 README.md 수행.
#### 3. catkin_make
```
$ catkin_make
$ devel/setup.bash
```
![catkin_make](https://user-images.githubusercontent.com/46383014/74773036-748a8180-52d4-11ea-9525-d722b1c4b610.png)
##### 위와 같이 실행되면 성공(package 이름은 carto_mapper)
#### 4. Start
```
roslaunch carto_mapper mapper.launch
```
##### 실행 초기 화면
###### 좌측 하단 Add를 클릭한 후 선택할 수 있는 새로운 창이 열리면 By topic으로 가서 map을 선택하면 실행됨.
![carto_mapper](https://user-images.githubusercontent.com/46383014/74772881-27a6ab00-52d4-11ea-8560-69eb8f37c5ab.png)
##### Map을 추가한 rviz 화면
![mapping](https://user-images.githubusercontent.com/46383014/74772888-28d7d800-52d4-11ea-86e0-ed633e76b4e1.png)
