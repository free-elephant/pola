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

***
## ** 하드웨어 프로세스 **
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

#### 6. 완료
