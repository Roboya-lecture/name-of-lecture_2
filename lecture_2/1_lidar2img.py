import pdb
import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm

def load_velodyne_points(filename):
    points = np.fromfile(filename, dtype=np.float32).reshape(-1, 4)
    points[:, 3] = 1.0 # homogeneous
    return points

img = cv2.imread('0.jpg')
lidar = load_velodyne_points('0.bin')

# Intrinsic
K = np.array([[0.58, 0, 0.5, 0],
              [0, 1.92, 0.5, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]], dtype=np.float32)
K[0] *= img.shape[1]
K[1] *= img.shape[0]

# Extrinsic
T = np.array([[ 6.09695409e+02, -7.21421597e+02, -1.25125855e+00, -1.67899086e+02],
              [ 1.80384202e+02,  7.64479802e+00, -7.19651474e+02, -1.01233067e+02],
              [ 9.99945389e-01,  1.24365378e-04,  1.04513030e-02, -2.72132796e-01]])

lidar2img_pts = np.dot(T, lidar.T).T
lidar2img_pts[:, :2] = lidar2img_pts[:, :2] / lidar2img_pts[:, 2][..., np.newaxis]

empty_img = np.zeros(img.shape[:-1])
for pt in lidar2img_pts:
if pt[-1] >= 0.0:
if (pt[0] >= 0 and pt[0] < img.shape[1]) and (pt[1] >= 0 and pt[1] < img.shape[0]):
empty_img[int(pt[1]),int(pt[0])] = pt[-1]

normalizer = mpl.colors.Normalize(vmin=empty_img.min(), vmax=empty_img.max())
mapper = cm.ScalarMappable(norm=normalizer, cmap='jet')
colormapped_im = (mapper.to_rgba(empty_img)[:, :, :3] * 255).astype(np.uint8)
colormapped_im[empty_img == 0] *= 0
img[empty_img > 0] *= 0
fuse_map = colormapped_im + img
cv2.imwrite('fuse_map.png',fuse_map)




