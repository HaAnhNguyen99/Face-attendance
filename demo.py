import  cv2
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    cv2.imshow('webcam', img)
    key = cv2.waitKey(1)
    if key % 256 == 27:
        break
cap.release()
cv2.destroyAllWindows()