# 1. INTRO


software
--------
 - ububtu 18.04
 - ROS melodic
 - python 3.6
 - python 2.7 on Ros
 - Realsense adk 2.0
 - Tensorflow 1.4
 - opencv 3.4
 - pytorch 1.2
 - catographer
 - cuda

Hardware
--------
 - Rasberry Pi4
 - Intel Realsense Camera 435i
 - Ydlidar G2
 - BLDC모터 (PG42-BL4261)
 - BLDC모터드라이버 (BDC-15) 
 - 기어모터 고정브라켓 (GMB-42M)
 - 알루미늄 프로파일
 - 큐브프레임 (MDF 합판)
 - 오프로드바퀴 (130파이)
 - 연축전지 12V
 - 보조배터리(output:3A)

# ** 하드웨어 프로세스 **
### 1. 도서관 환경 사전 조사
#### -구조 및 장애물 파악
#### -프로젝트 목표에 부합하는 요건 조사
### 2. 설계도 구상과 지속적인 피드백 및 수정
#### -레이저 커팅기 사용을 위한 Tool(Rhino) 사용
#### -Rhino로 POLA 도면 작성
#### -제작 과정 중 오차 및 error 사항 파악 및 수정
### 3. 구입 목록 작성 및 주문
#### -필요 물품 구입
### 4. 제작 및 시행착오
#### -알루미늄 프로파일 크기 및 무게 오계산
#### -Jetson nano의 GPU 사용위해 선택
#### -But, PWM 사용 불확실 및 GPIO(PWM Channel: 2개) 채널 부족 -> Rasberry Pi4 선택
#### -초기 구매 모터드라이버(아날로그만 지원과 명확한 상세 설명 부족 및 Data sheet 부재)
#### -외부 MCU 제어(PWM) 가능한 모터드라이버로 교체
#### -Rasberry Pi4 2.5A 이상에서 안정적으로 작동 가능함(전류 부족 시 Shut down)
### 5. Testing 및 개선

### 6. 완료
