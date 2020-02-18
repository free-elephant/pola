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
catkin_make_isolated --install --use-ninja
```
***
## YDLIDAR G2 - Hector Slam Example
#### 설치한 Google Cartographer 를 이용해서 Hector Slam 을 구현해본다. 

#### 1. git clone해서 src directory로 복사
```
