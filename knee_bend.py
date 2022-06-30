from itertools import count
import cv2
import mediapipe as mp
import numpy as np
import time
import pose_module as pm

#capture the video
cap = cv2.VideoCapture('D:\\OpenCV\\Assignment\\KneeBendVideo.mp4')

#use customemade poseDetector module
detector = pm.poseDetector()
dir = "straight"
pTime = 0
start_time = 0
bend_time = 0
count = 1
while True:
    start_time = 0
    start_time = time.time()
    success,img = cap.read()
    

    img = cv2.resize(img,(700,600))
    img=detector.findPose(img,False)
    lmList = detector.findPosition(img,False)

    #print(lmList)
    if len(lmList)!=0:
        angle = detector.findAngle(img,23,25,27) #find the angle bew landmarks
        per = np.interp(angle,(66,175),(0,100)) #convert range of angle into percentage
        #print(angle,per)
        if per < 68 :#check weather angle <140
            bend_time += time.time()-start_time
            #bend_time = round(bend_time,0)
            print(round(bend_time,1))
            cv2.putText(img,"Counter:"+f'{int(bend_time)}',(30,190),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            if bend_time>8:
                cv2.rectangle(img,(240,50),(650,120),(255,255,255),0)
                cv2.putText(img,"Very Good Form",(250,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),3)

            if dir == "bend":
                count+=0.5
                
                dir = "straight"


        if per >68: #check wheather angle > 140

            if dir == "straight":
                start = time.time()
                count+=0.5
                dir = "bend"

                if bend_time < 8:
                    cv2.putText(img,"Keep your knee bent",(50,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),3)
                    count-=1

            bend_time=0
                
        

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,"FPS:"+str(int(fps)),(10,50),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),2)
        cv2.putText(img,"RAPS:"+f'{int(count)}',(30,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)

    cv2.imshow("image",img)    

    cv2.waitKey(1)

cv2.destroyAllWindows()    

