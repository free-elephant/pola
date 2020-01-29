# **Ydlidar ROS Package install**

### 1. Ros package 를 저장할 디렉토리 생성
```
$ mkir -p ~/ydlidar_ws/src
```

### 2. ~/ydlidar_ws/src 안에 ydlidar package를 git에서 다운로드
```
$ cd ~/ydlidar_ws/src
$ sudo git clone https://github.com/YDLIDAR/ydlidar.git
```

### 3. git에서 다운받은 것들을 초기상태로 커밋
```
$ sudo git checkout gaussian
```

### 4. git submodule 지정
```
$ cd ~/ydlidar_ws/src/ydlidar/sdk
$ git submodule init
$ git submodule update
```

### 5. catkin make (catkin 빌드 시스템에 기반을 둔 빌드 - build, devel, src directory가 만들어짐.)
```
$ cd ~/ydlidar_ws
$ catkin_make ydlidar
```
## SCREEN SHOT
![catkin_make](./home/pirl/Slam/catkin_make.png)
### +++ processing catkin package : 'ydlidar_ros' >> 내가 생성한 ros package

### **주의 해야 할 점**
#### 확실하진 않지만 이 과정을 거치면서 /dev directory 안에 ydlidar file이 생성되어있어야함.
```
$ cd /dev
$ ls

# 두 코드를 입력했을 때 ydlidar라는 이름의 파일을 찾을 수 있어야함.
```

### 6. ydlidar 환경 변수를 bashrc file 안에 추가
```
$ echo "source ~/ydlidar_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

### 7. 
