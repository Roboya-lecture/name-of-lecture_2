import cv2

src = cv2.imread('roboya_img.jpg')
tgt = cv2.imread('roboya_lenna.png')

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
tgt_gray = cv2.cvtColor(tgt, cv2.COLOR_BGR2GRAY)

detector = cv2.SIFT_create()

kp1, desc1 = detector.detectAndCompute(src_gray, None)
kp2, desc2 = detector.detectAndCompute(tgt_gray, None)

matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

matches = matcher.match(desc1, desc2)

res = cv2.drawMatches(src, kp1, tgt, kp2, matches, \
None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imwrite('match.png', res)

