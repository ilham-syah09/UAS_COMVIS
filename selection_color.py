import cv2
import numpy as np

def nothing(x):
    pass

# set trackbar
hh = 'hue high'
hl = 'hue low'
sh = 'saturation high'
sl = 'saturation low'
vh = 'value high'
vl = 'value low'

#set nama window untuk trackbar
cv2.namedWindow('threshold')

# set range trackbar
cv2.createTrackbar(hh, 'threshold', 179, 179, nothing)
cv2.createTrackbar(hl, 'threshold', 0, 179, nothing)
cv2.createTrackbar(sh, 'threshold', 255, 255, nothing)
cv2.createTrackbar(sl, 'threshold', 0, 255, nothing)
cv2.createTrackbar(vh, 'threshold', 255, 255, nothing)
cv2.createTrackbar(vl, 'threshold', 0, 255, nothing)

#load image
img=cv2.imread('rainbow.png')

while(1):

    #mengambil nilai posisi terakhir dari trackbar
    hul = cv2.getTrackbarPos(hl, 'threshold')
    huh = cv2.getTrackbarPos(hh, 'threshold')
    sal = cv2.getTrackbarPos(sl, 'threshold')
    sah = cv2.getTrackbarPos(sh, 'threshold')
    val = cv2.getTrackbarPos(vl, 'threshold')
    vah = cv2.getTrackbarPos(vh, 'threshold')

    #mengelompokkan nilai threshold dari batas bawah dan batas atas
    #kedalam variabel array 
    hsvl=np.array([hul,sal,val],np.uint8)
    hsvh=np.array([huh,sah,vah],np.uint8)

    #mengkonversi colorspace atau ruang warna dari RGB ke HSV
    hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #memasang atau menerapkan threshold untuk HSV
    mask = cv2.inRange(hsv,hsvl,hsvh)

    #masking image 
    res = cv2.bitwise_and(img, img, mask=mask)

    #menampilkan image 
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    #tekan q untuk close program
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()
Python
