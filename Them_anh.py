import time
import cv2
name = "Khánh"
# cv2.namedWindow("Press Space to capture")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_counter = 0
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,255), 2)

        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Press Space to capture", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cam.release()
            cv2.destroyAllWindows()
            break

        elif k%256 == 32:
            # SPACE pressed

            t = time.strftime("%H-%M-%S")

            img_name = 'C:/Users/HA_ANH/PycharmProjects/Recognition/ImagesAttendance/'+ name +'.jpg'
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
