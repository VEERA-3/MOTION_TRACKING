#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
cap = cv2.VideoCapture('walking.mp4')
lk_params = dict(winSize=(15,15),
                maxLevel=2,
                criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))
color = (0,255,0)
ret,old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray,100,0.3,7,blockSize=7)
mask = np.zeros_like(old_frame)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    p1,st,err = cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p0,None,**lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]
    
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask,(int(a),int(b)),(int(c),int(d)),color,2)
        frame = cv2.circle(frame,(int(a),int(b)),5,color,-1)
    img = cv2.add(frame,mask)
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
    cv2.imshow('frame',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    


# In[ ]:




