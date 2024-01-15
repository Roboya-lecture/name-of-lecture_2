import numpy as np
import cv2
import torch
import torchvision.models as models

cat = cv2.resize(cv2.imread('cat.jpg'), (384, 384)).astype(np.float32) / 255.0
dog = cv2.resize(cv2.imread('dog.jpg'), (384, 384)).astype(np.float32) / 255.0

CAT, DOG = 1.0, 0.0
device = 'cuda'
data = torch.cat([torch.tensor(cat).permute(2,0,1)[None,...],
torch.tensor(dog).permute(2,0,1)[None,...]], dim=0).to(device)

resnet = models.resnet34(True)
resnet.fc = torch.nn.Linear(512,1)
resnet = torch.nn.Sequential(resnet, torch.nn.Sigmoid())
resnet.to(device)

optimizer = torch.optim.Adam(resnet.parameters(), 1e-5)
loss_func=torch.nn.BCELoss() 
target = torch.tensor([CAT, DOG]).type(torch.FloatTensor).to(device)[...,None]

for i in range(500):
  pred = resnet(data)
  loss = loss_func(pred, target)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  print(i, loss)

with torch.no_grad():
  v = resnet(data)
  print('cat') if v[0] > 0.5 else print('dog’)
  print('cat') if v[1] > 0.5 else print('dog')


