import cv2

cap = cv2.VideoCapture(0)

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
    cv2.imshow('Video Window Part', re_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()