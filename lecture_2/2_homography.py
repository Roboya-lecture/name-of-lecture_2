import cv2
import numpy as np


def Get_A_Matrix(dots):
    A = []
    for dot in dots:
        A.append([dot[0], dot[1], dot[2], 0, 0, 0,
                 -(dot[0] * dot[3]), -(dot[1] * dot[3]), -dot[3]])
        A.append([0, 0, 0, dot[0], dot[1], dot[2],
                 -(dot[0] * dot[4]), -(dot[1] * dot[4]), -dot[4]])
    return A

def Make_H(A,b):
    A = np.array(A)
    b = np.array(b)
    b = b.T
    b = np.dot(A.T, b)
    ATA_inv = np.linalg.inv(np.dot(A.T, A))
    H = np.dot(ATA_inv, b) #h = inv(A.T * A) * A.T * b
    H = np.array([[H[0], H[1], H[2]],
                  [H[3], H[4], H[5]],
                  [H[6], H[7], 1]])
    return H


src = cv2.imread('test1.jpg')
tgt = cv2.imread('test2.png')

h,w,c = src.shape

src_dot1 = np.array([[193, 281, 1], [437, 585, 1],
                     [477, 171, 1], [778, 367, 1]])
tgt_dot2 = np.array([[121, 344, 1], [738, 574, 1],
                     [370, 125, 1], [829, 243, 1]])
color = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)) #LT LB RT RB

for i in range(4):
   src = cv2.circle(src, (src_dot1[i,0],src_dot1[i, 1]), 5, color[i], -1)
   tgt = cv2.circle(tgt, (tgt_dot2[i,0],tgt_dot2[i, 1]), 5, color[i], -1)

A, b = Get_A_b_Matrix(np.concatenate((src_dot1, tgt_dot2), axis=1))
H = Make_H(A,b)

out = cv2.warpPerspective(src, H,(w, h))
cv2.imwrite('out.png',out)




