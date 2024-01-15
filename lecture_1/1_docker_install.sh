# 업데이트
# 업데이트
sudo apt update

# 설치에 필요한 패키지 설치
sudo apt install apt-transport-https ca-certificates curl software-properties-common

#도커 공식 GPG 키와 저장소 추가
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add – 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable”

# 도커 패키지가 검색되는지 확인
sudo apt update
sudo apt-cache search docker-ce
###### 현재 우분투 버전에서 설치 패키지가 검색 된다면, 아래와 같이 출력됨.
###### docker-ce - Docker: the open-source application container engine

# 도커-CE 설치
sudo apt install docker-ce 

#  도커 그룹에 사용자 추가, 도커 루트 권한 에러 해결 
sudo usermod -aG docker $USER 

