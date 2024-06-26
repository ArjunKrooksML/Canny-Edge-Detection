import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cannyedges = cv2.Canny(gray, 100, 200)

    cv2.imshow('Canny', cannyedges)

    if cv2.waitKey(1) & 0xFF == ord('`'):
        break

cap.release()
cv2.destroyAllWindows()



