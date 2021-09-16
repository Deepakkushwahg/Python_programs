import cv2
cap = cv2.VideoCapture("venv\images\kedarnath.mp4")
while 1:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break