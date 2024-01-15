import numpy as np
import cv2
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model = torch.hub.load("intel-isl/MiDaS", 'DPT_Hybrid').to(device)
model.eval()

img = cv2.cvtColor(cv2.imread('robot.png'), cv2.COLOR_BGR2RGB)
transform = torch.hub.load("intel-isl/MiDaS", "transforms").dpt_transform

img_tensor = transform(img).to(device)

with torch.no_grad():
    prediction = model(img_tensor)
    prediction = torch.nn.functional.interpolate(
                                  prediction.unsqueeze(1),
                                  size=img.shape[:2],
                                  mode="bicubic",
                                  align_corners=False).squeeze()


output = prediction.cpu().numpy()
max_v, min_v = output.max(), output.min()
save_output = 65535 * (output - min_v) / (max_v - min_v) 
cv2.imwrite(f'robot_depth.png', save_output.astype(np.uint16).reshape(save_output.shape[0],save_output.shape[1],1))






