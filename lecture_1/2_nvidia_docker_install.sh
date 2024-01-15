# 재부팅
sudo service docker restart 
# sudo systemctl reboot 

# Nvidia-docker2 설치 
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f sudo apt-get purge -y nvidia-docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) 
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - 
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list 

sudo apt-get update && sudo apt-get install nvidia-docker2 
sudo systemctl restart docker 

# 설치 여부 검증하기 (docker version 명령어를 쳐서 version확인)
# docker version 19.03 이상
docker run --gpus all nvidia/cuda:11.1-base nvidia-smi

# docker version 19.03 미만
# docker run --runtime=nvidia nvidia/cuda:11.1-base nvidia-smi

