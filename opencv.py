import cv2
import numpy as np

""" cap = cv2.VideoCapture(0)

if not cap.isOpened:
    print("Cannot read a Video.")
    exit()

while True:
    retVal, frame = cap.read()
    re_frame = frame[0:300][0:300]
    if not retVal:
        print("Exit")
        break

    # re_img = cv2.resize(img, (512, 512))
    cv2.imshow('Video Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release() """
image = cv2.imread("test3.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
""" result = np.zeros((image.shape[0], 256), dtype=np.uint8)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX) """
dst = []
dst2 = []
for i in range(3):
    result = np.zeros((image.shape[0], 256), dtype=np.uint8)
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    cv2.normalize(hist, hist, 0, image.shape[0], cv2.NORM_MINMAX)
    for x, y in enumerate(hist):
        print(x, y)
        cv2.line(result, (x, image.shape[0]), (x, image.shape[0]-int(y)), 255)
    dst.append(np.hstack([image[:,:,i], result]))
    print("image shape: ", image[:,:,i].shape)

final_dst = np.hstack(dst)
blue_only = np.zeros_like(image)
blue_only[:, :, 0] = image[:, :, 0]
print("blue shape: ", blue_only.shape)
dst2.append(blue_only)
green_only = np.zeros_like(image)
green_only[:, :, 1] = image[:, :, 1]
dst2.append(green_only)
red_only = np.zeros_like(image)
red_only[:, :, 2] = image[:, :, 0]
dst2.append(red_only)
final_dst2 = np.hstack(dst2)

cv2.imshow("ori", image)
cv2.imshow("dst", final_dst)
cv2.imshow("Real Light", final_dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()