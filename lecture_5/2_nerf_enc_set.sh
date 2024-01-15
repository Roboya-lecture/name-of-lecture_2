# 필수파일 설치 및 Code 다운로드
git clone https://github.com/yenchenlin/nerf-pytorch.git
cd nerf-pytorch
pip install -r requirements.txt 

# Dataset 설치 (Lego)
bash download_example_data.sh

# 학습 (2080Ti 기준 4시간)
# python run_nerf.py --config configs/lego.txt

