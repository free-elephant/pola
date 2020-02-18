# 1. INTRO

***
software
--------
 - UBUNTU 18.04 LTS
 - ROS Melodic
 - Python 3.6
 - Python 2.7 on Ros Platform
 - Realsense sdk-2.0
 - Tensorflow-gpu 1.4
 - Opencv 3.4
 - Pytorch 1.2
 - Cartographer
 - Cuda & Cuda toolkit 10.0
 - CuDnn 7.6.1
***
Hardware
--------
 - Rasberry Pi 4
 - Intel Realsense Camera 435i
 - Ydlidar G2
 - GeForce RTX 2080 * 2
 - BLDC모터 (PG42-BL4261)
 - BLDC모터드라이버 (BDC-15) 
 - 기어모터 고정브라켓 (GMB-42M)
 - 알루미늄 프로파일
 - 큐브프레임 (MDF 합판)
 - 오프로드바퀴 (130파이)
 - 연축전지 12V
 - 보조배터리(output:3A)
***
## Install Before Starting 
#### 메인 서버에 필수적인 파일들을 설치하고자 함. 
#### 기존에 CUDA 10.0 은 설치되어있었기 때문에 CUDA Toolkit부터 설치함.
#### anaconda 가상환경을 쓰지 않고, virtualenv 가상환경을 사용.
***
### ML Package Focus: CUDA10, cuDNN7.5, Tensorflow-gpu 1.14, Keras, Opencv3.4, PyTorch1.2.
### 1. Ubuntu Setup
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install build-essential cmake unzip pkg-config
$ sudo apt-get install libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran
$ sudo apt-get install libhdf5-serial-dev graphviz
$ sudo apt-get install python3-dev python3-tk python-imaging-tk
$ sudo apt-get install -y linux-image-generic linux-image-extra-virtual
$ sudo apt-get install -y linux-source linux-headers-generic
```
### 2. Nvidia(CUDA Toolkit, cuDnn)
#### 2.1 Nvidia 저장소 추가
```
$ sudo add-apt-repository ppa:graphics-drivers/ppa
$ sudo apt-get update
```
#### 2.2 Install CUDA Toolkit
##### - CUDA 10.0: https://developer.nvidia.com/cuda-10.0-download-archive (download) 
```
$ cd ~
$ cd Downloads
$ chmod +x cuda_10.0.130_410.48_linux.run 
$ sudo ./cuda_10.0.130_410.48_linux.run — override
```
##### - [space bar] 를 입력하면 설명 쭉 내려감. 
##### - "Install NVIDIA Accelerated Graphics Driver" 를 묻는 질문이 나오면 [n]을 입력.(나중에 따로 설치함)
##### - 나머지는 전부 [y] 입력.
#### 2.3 Add CUDA to Envirtoment Path
```
$ gedit ~/.bashrc 

# bashrc 창이 열리면 밑에 있는 것을 복사해서 붙여넣음. 
---------------------------
# NVIDIA CUDA Toolkit
export PATH=/usr/local/cuda-10.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64
---------------------------
# save 하고 난 뒤 끄기

$ source ~/.bashrc
```
#### 2.4 Check CUDA toolkit
```
$ nvcc -V
```
![cudatoolkit](https://user-images.githubusercontent.com/46383014/74749883-2febef80-52ae-11ea-9654-cbd351fab060.png)
##### 위와 같이 나오면 성공

### 3. Install cuDNN
#### - Signup & download cuDNN: https://developer.nvidia.com/cudnn (회원가입 필수)
#### - Downloads ".tgz" file
```
$ tar -zxf cudnn-10.0-linux-x64-v7.6.1.34.tgz
$ cd cuda
$ sudo cp -P lib64/* /usr/local/cuda/lib64/
$ sudo cp -P include/* /usr/local/cuda/include/
$ cd ~
```
### 4. Virtual Environment
#### 4.1 Install Virtual Environment
```
$ sudo apt install python3-testresources
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/get-pip.py ~/.cache/pip
```
#### 4.2 Add Environment Path
```
$ gedit ~/.bashrc 

# bashrc 창이 열리면 밑에 있는 것을 복사해서 붙여넣음. 
---------------------------
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
---------------------------
# save 하고 난 뒤 끄기

$ source ~/.bashrc
```
#### 4.3 Create Virtual Environment & Check VE
```
$ mkvirtualenv cv4 -p python3
$ workon cv
```
### 5.0 Install Tensorflow-gpu + keras
#### 5.1 pip Install Python libraries
```
$ pip install numpy
$ pip install pandas scipy matplotlib pillow
$ pip install scikit-learn scikit-image
$ pip install tensorflow-gpu==1.14.0
$ pip install keras
$ pip install imutils h5py requests progressbar2
```
##### - opencv 와 pytorch는 나중에 설치할 것이기 때문에 지금 설치하면 안됨.
#### 5.2  Check Tensorflow gpu enabled or disabled
```
$ python
>>> import tensorflow as tf
>>> tf.test.is_gpu_available()
True or False

# 만약에 false 가 나오면 gpu 사용이 안되는 상태니 다시 설치하거나 오류 수정해야함.
```
### 6. Install OpenCV

##### OpenCV 를 최신 버전이 아닌 3.4 버전을 설치하는 이유는 Realsense 관련 패키지를 catkin_make 할 때 OpenCV가 필요한데 3.x 버전을 필요로 한다고 출력되고, 4.0.1 버전을 설치하면 catkin_make .
#### 6.1 Install dependencies
```
$ sudo add-apt-repository "deb http://security.ubuntu.com ubuntu xenial-security main"
$ sudo apt update
$ sudo apt install libjasper1 libjasper-dev
$ sudo apt-get update && sudo apt-get upgrade — fix-missing — fix-broken
$ sudo apt-get install libgtk2.0-dev
$ sudo apt -y install python3-dev python3-pip python3-vev
sudo -H pip3 install -U pip numpy
sudo apt -y install python3-testresources
```
#### 6.2 Downloads Files OpenCV github
```
$ cd ~
$ git clone https://github.com/opencv/opencv.git
$ cd opencv
$ cd ..
$ git clone https://github.com/opencv/opencv_contrib.git
$ cd opencv_contrib
$ cd ..
```
#### 6.3 Make directory
```
$ cd ~/opencv
$ mkdir build
$ cd build
```
#### 6.4 Prepare to Compile
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
 -D WITH_CUDA=ON \
 -D BUILD_NEW_PYTHON_SUPPORT=ON \
 -D BUILD_PYTHON_SUPPORT=ON \
 -D INSTALL_PYTHON_EXAMPLES=ON \
 -D INSTALL_C_EXAMPLES=ON \
 -D BUILD_EXAMPLES=ON \
 -D OPENCV_ENABLE_NONFREE=ON \
 -D BUILD_opencv_cudacodec=OFF \
 -D ENABLE_FAST_MATH=1 \
 -D CUDA_FAST_MATH=1 \
 -D WITH_OPENGL=ON \
 -D WITH_TBB=ON \
 -D WITH_V4L=ON \
 -D WITH_QT=ON \
 -D WITH_GTK=ON \
 -D BUILD_opencv_python3=ON \
 -D PYTHON_EXECUTABLE=~/.virtualenvs/cv4/bin/python3.6 ..
```
![aa](https://user-images.githubusercontent.com/46383014/74754241-aab80900-52b4-11ea-8b63-734668e0caec.png)
##### 위와 같이 출력되면 성공.
#### 6.5 Compilation
```
# 컴퓨터에 따라 다르지만 약 1시간 정도 소요됨.

$ make -j8

# 8은 코어수
# 코어를 확인하려면
# $ grep -c processor /proc/cpuinfo

$ sudo make install
$ sudo ldconfig
```
#### 6.6 Rename the file 
```
$ cd /usr/local/lib/python3.6/site-packages/cv2/python-3.6
$ sudo mv cv2.cpython-36m-x86_64-linux-gnu.so cv2.so
```
#### 6.7 Copy cv2.so to Virtual Enviornment 
```
$ cd ~/.virtualenvs/cv4/lib/python3.6/site-packages/
$ ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.so cv2.so
```
#### 6.8 Check OpenCV
```
$ workon cv4
$ python
>>> import cv2
>>> cv2.__verion__
```
![opencv](https://user-images.githubusercontent.com/46383014/74755565-b60c3400-52b6-11ea-9a15-5bc09ef68694.png)
##### 위와 같이 출력되면 성공.

### 7. Install Pytorch
```
pip install torch==1.2.0 
pip install torchvision==0.4.0
```

***
## ** Hardware Process **
#### 1. 도서관 환경 사전 조사
##### -구조 및 장애물 파악
##### -프로젝트 목표에 부합하는 요건 조사
#### 2. 설계도 구상과 지속적인 피드백 및 수정
##### -레이저 커팅기 사용을 위한 Tool(Rhino) 사용
##### -Rhino로 POLA 도면 작성
##### -제작 과정 중 오차 및 error 사항 파악 및 수정
#### 3. 구입 목록 작성 및 주문
##### -필요 물품 구입
#### 4. 제작 및 시행착오
##### -알루미늄 프로파일 크기 및 무게 오계산
##### -Jetson nano의 GPU 사용위해 선택
##### -But, PWM 사용 불확실 및 GPIO(PWM Channel: 2개) 채널 부족 -> Rasberry Pi4 선택
##### -초기 구매 모터드라이버(아날로그만 지원과 명확한 상세 설명 부족 및 Data sheet 부재)
##### -외부 MCU 제어(PWM) 가능한 모터드라이버로 교체
##### -Rasberry Pi4 2.5A 이상에서 안정적으로 작동 가능함(전류 부족 시 Shut down)
#### 5. Testing 및 개선
(추가될 예정)
#### 6. 완료
(추가될 예정)
