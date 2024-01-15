# Code 다운로드 (Git clone)
git clone https://github.com/taesungp/contrastive-unpaired-translation CUT 
cd CUT

# 데이터 다운로드
bash ./datasets/download_cut_dataset.sh grumpifycat

# 학습
# python train.py --dataroot ./datasets/grumpifycat --name grumpycat_FastCUT --CUT_mode FastCUT

# 이미지 생성
# python test.py --dataroot ./datasets/grumpifycat --name grumpycat_CUT --CUT_mode CUT --phase train

