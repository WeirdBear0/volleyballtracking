import cv2
import time
import math

p1 = 530
p2 = 300
xArr = []
yArr = []

video = cv2.VideoCapture("footvolleyball.mp4")

tracker = cv2.TrackerCSRT_create()
ret, img = video.read()
boundingBox = cv2.selectROI("footvolleyball", img, False)
tracker.init(img, boundingBox)

def drawBox(img, box):
    x,y,w,h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 2)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

def trackGoal(img, box):
    x,y,w,h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img, (c1,c2), 2, (255,255,255), 5)
    cv2.circle(img, (int(p1),int(p2)), 2, (255,255,255), 5)

    # dist = math.sqrt(((c1-p1)**2) + ((c2-p2)**2))
    # if(dist <= 15):
    #     cv2.putText(img, "Goal", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    xArr.append(c1)
    yArr.append(c2)
    for i in range(len(xArr)-1):
        cv2.circle(img, (xArr[i], yArr[i]), 2, (255,255,255), 5)


while True:
    check,img = video.read()   
    success, boundingBox = tracker.update(img)
    if success:
        drawBox(img, boundingBox)
    else:
        cv2.putText(img, "Lost", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    
    trackGoal(img, boundingBox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == ord('q'):
        print("Stopped!")
        break


video.release()
cv2.destroyAllWindows()



