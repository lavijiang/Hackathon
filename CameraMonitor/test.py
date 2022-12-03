import cv2

img = cv2.imread("Hackathon/Camera/pics/person.jpg")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
bodies = body_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 5)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()